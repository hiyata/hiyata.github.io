#!/usr/bin/env python3
"""Fetch the PubMed and arXiv feeds server-side and write them as static JSON.

Runs from a scheduled GitHub Action rather than the browser, since neither
pubmed.ncbi.nlm.nih.gov nor export.arxiv.org send Access-Control-Allow-Origin
headers, so a direct browser fetch from the site is blocked by CORS. Fetching
here avoids depending on a third-party CORS proxy and needs no API key.
"""

import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html import unescape

PUBMED_RSS_URL = (
    "https://pubmed.ncbi.nlm.nih.gov/rss/search/"
    "1xCFUMSbAMYitB6LKyB5opiesUFp1inW-kMm4Ly8hr-nJYagWd/"
    "?limit=15&utm_campaign=pubmed-2&fc=20240820105625"
)
ARXIV_QUERY = (
    'all:("genomic language model" OR "genomic LLM" OR "genomics LLM" '
    'OR "genomics language model" OR (genomic AND "large language model"))'
)
ARXIV_API_URL = (
    "https://export.arxiv.org/api/query?search_query="
    + urllib.parse.quote(ARXIV_QUERY)
    + "&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results=8"
)

USER_AGENT = "hiyata.github.io-feed-updater/1.0 (+https://hiyata.github.io)"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
TAG_RE = re.compile(r"<[^>]+>")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()


def strip_html(text, limit=220):
    text = unescape(TAG_RE.sub(" ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0] + "..."
    return text


def build_payload(items):
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "items": items,
    }


def write_json(path, payload):
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def update_pubmed():
    xml_bytes = fetch(PUBMED_RSS_URL)
    root = ET.fromstring(xml_bytes)
    items = []
    for item in root.findall(".//item")[:8]:
        title = strip_html((item.findtext("title") or "").strip(), limit=200)
        link = (item.findtext("link") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()
        description = strip_html(item.findtext("description") or "")
        if not title or not link:
            continue
        items.append(
            {
                "title": title,
                "link": link,
                "date": pub_date,
                "summary": description,
            }
        )
    if not items:
        raise RuntimeError("parsed zero PubMed items, refusing to overwrite")
    write_json("assets/data/pubmed-feed.json", build_payload(items))
    print(f"pubmed: wrote {len(items)} items")


def update_arxiv():
    xml_bytes = fetch(ARXIV_API_URL)
    root = ET.fromstring(xml_bytes)
    items = []
    for entry in root.findall("atom:entry", ATOM_NS)[:8]:
        title = strip_html((entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip(), limit=200)
        link = (entry.findtext("atom:id", default="", namespaces=ATOM_NS) or "").strip()
        published = (entry.findtext("atom:published", default="", namespaces=ATOM_NS) or "").strip()
        summary = strip_html(entry.findtext("atom:summary", default="", namespaces=ATOM_NS) or "")
        authors = [
            (a.findtext("atom:name", default="", namespaces=ATOM_NS) or "").strip()
            for a in entry.findall("atom:author", ATOM_NS)
        ]
        if not title or not link:
            continue
        items.append(
            {
                "title": title,
                "link": link,
                "date": published,
                "authors": [a for a in authors if a],
                "summary": summary,
            }
        )
    write_json("assets/data/arxiv-feed.json", build_payload(items))
    print(f"arxiv: wrote {len(items)} items (0 is a valid result for this niche query)")


def main():
    failures = []
    for name, fn in (("pubmed", update_pubmed), ("arxiv", update_arxiv)):
        try:
            fn()
        except Exception as exc:  # noqa: BLE001
            failures.append(name)
            print(f"{name}: FAILED - {exc}", file=sys.stderr)

    if failures:
        # Non-zero exit surfaces the failure in the Actions run, but any feed
        # that succeeded above has already been written, and any feed that
        # failed simply leaves its last committed JSON file untouched.
        sys.exit(1)


if __name__ == "__main__":
    main()
