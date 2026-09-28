"""Fetch openly-licensed images from Wikimedia Commons and record their attribution.

Usage:
    python3 tools/nbme-micro/fetch_images.py wanted.tsv
    python3 tools/nbme-micro/fetch_images.py --check      # re-verify credits.json

Each line of the TSV is:   localname.jpg <TAB> File:Some Commons Title.jpg

The script asks the Commons API for the file's licence, author, and description
page, refuses anything that is not public domain / CC0 / CC BY / CC BY-SA,
downloads a width-limited copy, and writes the attribution into credits.json.
The build refuses to attach any figure that has no credits.json entry, so the
licence and author always travel with the picture onto the page.
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
IMG_DIR = os.path.join(REPO, "assets/images/nbme/micro")
CREDITS = os.path.join(HERE, "credits.json")
API = "https://commons.wikimedia.org/w/api.php"
UA = "hiyata-nbme-micro/1.0 (educational question bank; https://hiyata.github.io)"
WIDTH = 1100

# Only these licences may be attached. Anything else is skipped and reported.
OK_LICENCE = ("cc0", "cc by", "cc by-sa", "public domain", "pd")


def _get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read() if binary else json.loads(r.read())


def _strip(html):
    """Commons returns author/description as small HTML fragments."""
    import re
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = text.replace("&amp;", "&").replace("&quot;", '"').replace("&#039;", "'")
    return " ".join(text.split())


def licence_ok(lic):
    low = (lic or "").strip().lower()
    return any(low.startswith(p) for p in OK_LICENCE)


def lookup(title):
    q = {"action": "query", "titles": title, "prop": "imageinfo", "format": "json",
         "iiprop": "url|extmetadata|size|mime", "iiurlwidth": str(WIDTH)}
    data = _get(API + "?" + urllib.parse.urlencode(q))
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()), {})
    if "imageinfo" not in page:
        return None, "not found on Commons"
    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})
    lic = _strip(meta.get("LicenseShortName", {}).get("value"))
    if not licence_ok(lic):
        return None, f"licence not permitted: {lic or 'unknown'}"
    if info.get("mime") not in ("image/jpeg", "image/png"):
        return None, f"unsupported type {info.get('mime')}"
    return {
        "url": info.get("thumburl") or info["url"],
        "title": page.get("title", title),
        "lic": lic,
        "artist": _strip(meta.get("Artist", {}).get("value")) or "Unknown",
        "page": info.get("descriptionurl", ""),
    }, None


def main():
    credits = json.load(open(CREDITS)) if os.path.exists(CREDITS) else {}
    os.makedirs(IMG_DIR, exist_ok=True)

    if "--check" in sys.argv:
        missing = [f for f in credits if not os.path.exists(os.path.join(IMG_DIR, f))]
        bad = [f for f, c in credits.items() if not licence_ok(c.get("lic"))]
        extra = sorted(set(os.listdir(IMG_DIR)) - set(credits))
        print(f"{len(credits)} credits, {len(os.listdir(IMG_DIR))} files")
        if missing: print("credited but not downloaded:", missing)
        if bad: print("LICENCE NOT PERMITTED:", bad)
        if extra: print("file with no credit:", extra)
        if not (missing or bad or extra): print("credits and files agree")
        return

    wanted = []
    for path in [a for a in sys.argv[1:] if not a.startswith("-")]:
        for line in open(path):
            line = line.strip()
            if not line or line.startswith("#"): continue
            local, _, title = line.partition("\t")
            wanted.append((local.strip(), title.strip()))

    force = "--force" in sys.argv
    got = skipped = failed = 0
    for local, title in wanted:
        dest = os.path.join(IMG_DIR, local)
        if os.path.exists(dest) and not force:
            skipped += 1
            continue
        info, err = lookup(title)
        if err:
            print(f"  SKIP {local}: {err}")
            failed += 1
            continue
        try:
            blob = _get(info["url"], binary=True)
        except Exception as e:
            print(f"  SKIP {local}: download failed ({e})")
            failed += 1
            continue
        with open(dest, "wb") as f:
            f.write(blob)
        credits[local] = {k: info[k] for k in ("title", "lic", "artist", "page")}
        print(f"  ok   {local}  <- {info['title']}  [{info['lic']}]  {len(blob)//1024} KB")
        got += 1
        time.sleep(0.4)

    with open(CREDITS, "w") as f:
        json.dump(credits, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    print(f"fetched {got}, already present {skipped}, failed {failed}")


if __name__ == "__main__":
    main()
