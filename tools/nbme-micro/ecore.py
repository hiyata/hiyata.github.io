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


def E(eid, name, group, summary, quick=None, sections=None, images=None,
      aka=None, keywords=None, treatment=None):
    """One encyclopedia entry.

    quick:     ordered dict-like list of (label, value) shown as an at-a-glance table
    images:    list of (filename, caption); filenames must exist in credits.json
    aka:       other names the search box should match
    keywords:  extra search terms (diseases, buzzwords, toxins)
    treatment: one-line drug summary pinned under the title
    """
    return {
        "id": eid, "name": name, "group": group, "summary": summary,
        "aka": list(aka or []), "keywords": list(keywords or []),
        "treatment": treatment or "",
        "quick": [list(x) for x in (quick or [])],
        "images": [list(x) for x in (images or [])],
        "sections": list(sections or []),
    }
