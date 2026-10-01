"""Helpers for the microbiology encyclopedia.

An entry is one organism (or one tightly related group). Sections hold paragraphs;
a paragraph marked high-yield is what the page highlights when the reader ticks
"Step 1 high-yield". Everything else is the underlying science that explains why
the high-yield fact is true - that is the point of the two layers.
"""

def P(text):
    """An ordinary paragraph: mechanism, structure, the reasoning behind the fact."""
    return {"t": text, "hy": False}


def H(text):
    """A Step 1 high-yield paragraph - highlighted when the reader asks for it."""
    return {"t": text, "hy": True}


def S(heading, paras):
    return {"h": heading, "p": paras}


def TL(year, label, text="", img=None):
    """One timeline milestone, collapsed to `year` + `label` until the reader
    clicks it open, at which point `text` (a paragraph) is shown. `year` is a
    string so it can be a range or a qualifier ("1928", "1940s", "2003 (SARS)").
    `img` is an optional filename in assets/images/nbme/micro/ (must be
    credited in credits.json, same as a section figure) shown as the node's
    portrait/photo on the timeline rail.
    """
    return {"y": str(year), "label": label, "t": text, "img": img or ""}


def REVIEW(title, journal, year, url):
    """A specific, real, open-access review article. Never invent a url or a
    title: this field only exists for links that have actually been found and
    verified to resolve and to match the citation given.
    """
    return {"title": title, "journal": journal, "year": year, "url": url}


def HISTORY(paras, timeline=None):
    """The discovery story: what problem made people look, who found the
    answer and how, what they first thought it was, and how the picture
    was refined up to the present. `timeline` is an ordered list of TL(...).
    """
    return {"p": list(paras), "timeline": list(timeline or [])}


def RESEARCH(paras, reviews=None):
    """Where current understanding is unsettled or moving: open questions,
    recent mechanistic surprises, vaccine/therapeutic frontiers. `reviews` is
    a list of REVIEW(...) pointing to real open-access articles."""
    return {"p": list(paras), "reviews": list(reviews or [])}


def E(eid, name, group, summary, quick=None, sections=None, images=None,
      aka=None, keywords=None, treatment=None, history=None, research=None):
    """One encyclopedia entry.

    quick:     ordered dict-like list of (label, value) shown as an at-a-glance table
    images:    list of (filename, caption); filenames must exist in credits.json
    aka:       other names the search box should match
    keywords:  extra search terms (diseases, buzzwords, toxins)
    treatment: one-line drug summary pinned under the title
    history:   HISTORY(...) - discovery story and timeline; optional, collapsed
               below the Step 1 sections so it never competes with them
    research:  RESEARCH(...) - current frontiers and review-article links
    """
    return {
        "id": eid, "name": name, "group": group, "summary": summary,
        "aka": list(aka or []), "keywords": list(keywords or []),
        "treatment": treatment or "",
        "quick": [list(x) for x in (quick or [])],
        "images": [list(x) for x in (images or [])],
        "sections": list(sections or []),
        "history": history or {"p": [], "timeline": []},
        "research": research or {"p": [], "reviews": []},
    }
