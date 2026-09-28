# Micro question-bank source

The published bank is `assets/js/nbme/micro-data.js`, generated from these files.
Do not edit the generated file by hand.

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
  options, distractor explanations, tables). `retro_z*.py` (length-cue fixes) and
  `retro_f*.py` (figures and step walkthroughs) are later passes that merge into and
  override the `retro_s*` entries. All are keyed by the question's `topic` string.
- `credits.json` — source, author, and licence for every image and figure, keyed by
  filename. The build refuses to attach a figure that has no entry here.

## Explanation figures
`fig=F("fig-name.jpg", "caption")` attaches a teaching diagram to an explanation, and
`steps=[...]` adds a numbered walkthrough above it. Figures live in
`assets/images/nbme/micro/` with a `fig-` prefix. Every figure must be openly licensed
(public domain, CC0, CC BY, or CC BY-SA); the page prints its title, author, and licence
with a link to the source under the image, so attribution travels with the figure.

## Build
    python3 tools/nbme-micro/build.py      # rewrites assets/js/nbme/micro-data.js
    python3 tools/nbme-micro/build.py --strict   # also fail the build on length cues

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
