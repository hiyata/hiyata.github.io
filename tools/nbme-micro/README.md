# Micro question-bank and encyclopedia source

Two generated files, neither of which should be edited by hand:
- `assets/js/nbme/micro-data.js` — the question bank (`build.py`)
- `assets/js/nbme/micro-encyclopedia.js` — the encyclopedia (`build_encyclopedia.py`)

## Layout
- `qcore.py` — the `Q()` helper. **The correct answer is always `opts[0]`**; the builder
  moves it to a seeded-random letter, so the answer key is evenly spread and stable.
- `tables.py` — reusable comparison tables (`T(title, cols, rows)`) shared across explanations.
- `s01..s17_*.py` — the original questions.
- `n01..n15_*.py` — later questions. Any file matching `n##_*.py` is picked up automatically.
  `n08` onward go organism by organism in depth (staphylococci, streptococci, Gram-positive
  rods, Gram-negatives, mycobacteria and spirochetes, DNA viruses, RNA viruses and hepatitis,
  fungi and parasites), testing the same organism from several angles: lab identification,
  virulence mechanism, clinical syndrome, treatment, and epidemiology.
- `retro_s*.py` — per-question overlay for the original questions (difficulty, reworded
  options, distractor explanations, tables). `retro_z*.py` (cue fixes) and
  `retro_f*.py` (images, figures and step walkthroughs) are later passes that merge into
  and override the `retro_s*` entries. All are keyed by the question's `topic` string.
  An overlay may set `img` (a picture shown with the stem) as well as `fig` and `steps`.
- `credits.json` — source, author, and licence for every image and figure, keyed by
  filename. The build refuses to attach a figure that has no entry here.

## Explanation figures
`fig=F("fig-name.webp", "caption")` attaches a teaching diagram to an explanation, and
`steps=[...]` adds a numbered walkthrough above it. Figures live in
`assets/images/nbme/micro/` with a `fig-` prefix. Every figure must be openly licensed
(public domain, CC0, CC BY, or CC BY-SA); the page prints its title, author, and licence
with a link to the source under the image, so attribution travels with the figure.

## Encyclopedia
`ecore.py` defines the entry helpers and `e##_*.py` files hold the entries, which
`build_encyclopedia.py` assembles. Each entry has a summary, an at-a-glance `quick`
table, figures, and sections of paragraphs. `P(...)` is an ordinary paragraph —
the mechanism and structure that explain why something is true — and `H(...)` marks
a Step 1 high-yield paragraph. The page highlights the `H` layer, or shows it alone,
when the reader ticks "Step 1 high-yield". The build fails if an entry has no
high-yield paragraph, uses an unknown group, or references an uncredited image.

The encyclopedia opens from the setup screen and from the book button in the exam's
bottom toolbar. It is an overlay appended to `<body>`, so the exam's `render()` never
disturbs it and opening it mid-block leaves the timer, answers and flags untouched.
Opened during a block it also offers "Related to the question on screen" chips, matched
against the current item's stem, options and explanation. Ctrl/Cmd+K opens it anywhere.

## Images
`fetch_images.py` downloads figures from Wikimedia Commons and records attribution:

    python3 tools/nbme-micro/fetch_images.py wanted.tsv   # localname.webp <TAB> File:Commons Title.jpg
    python3 tools/nbme-micro/fetch_images.py --check      # credits.json vs files on disk

Downloads are re-encoded as WebP (a `.jpg` local name is rewritten to `.webp`).
It refuses any licence that is not public domain, CC0, CC BY, or CC BY-SA, and writes
the title, author, licence, and source page into `credits.json`. Both builds refuse to
attach an image with no credit, so attribution always reaches the page.

## Build
    python3 tools/nbme-micro/build.py             # rewrites micro-data.js
    python3 tools/nbme-micro/build.py --strict    # also fail on legacy length cues
    python3 tools/nbme-micro/build_encyclopedia.py  # rewrites micro-encyclopedia.js

## Checks the build runs
- every item has 5 options, no duplicate option text, no duplicate stems
- every referenced image exists in `assets/images/nbme/micro/`
- **answer cues**, so a test taker cannot score without reading the stem:
  - *key too long*: correct answer more than 15% and 10 characters longer than its longest
    distractor; *key too short*: the same margin below its shortest distractor.
  - *punctuation*: a parenthesis, semicolon, or colon appearing only in the key, which marks
    it as the option carrying the extra explanation.
  - *stem echo*: a distinctive word the key shares with the stem that no distractor uses.
  - Bank-wide "key is longest" and "key is shortest" rates are printed; target is about 20%
    each (chance). Run `build.py -v` to list the individual cues.
  Questions in `n08_*.py` and later **fail the build** on any of these; the older files only
  report them, and `retro_z*.py` passes fix them in place.
- `why` prefixes resolve to exactly one distractor; tables are well formed

## Gotcha
Tag constants in a question file must not shadow a table name imported from `tables.py`
(that is why the tag constants are named `TAG_*`).
