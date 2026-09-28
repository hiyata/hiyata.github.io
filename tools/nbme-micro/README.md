# Micro question-bank source

The published bank is `assets/js/nbme/micro-data.js`, generated from these files.
Do not edit the generated file by hand.

## Layout
- `qcore.py` — the `Q()` helper. **The correct answer is always `opts[0]`**; the builder
  moves it to a seeded-random letter, so the answer key is evenly spread and stable.
- `tables.py` — reusable comparison tables (`T(title, cols, rows)`) shared across explanations.
- `s01..s17_*.py` — the original questions.
- `n01..n07_*.py` — later questions. Any file matching `n##_*.py` is picked up automatically.
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
- **length cues**: flags any item whose correct answer is more than 15% and 10 characters
  longer than its longest distractor, and prints the bank-wide "key is longest" rate.
  Target is about 20% (chance). Keep distractors parallel in length to the key — a test
  taker must not be able to score by picking the longest option.
- `why` prefixes resolve to exactly one distractor; tables are well formed

## Gotcha
Tag constants in a question file must not shadow a table name imported from `tables.py`
(that is why the tag constants are named `TAG_*`).
