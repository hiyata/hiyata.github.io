"""Assemble the microbiology question bank into assets/js/nbme/micro-data.js.

Each section file defines QUESTIONS = [Q(...), ...]. In Q(), the correct option is
always listed first; the builder moves it to a seeded-random letter so the answer key
is evenly spread and stable across rebuilds.
"""
import importlib, json, os, random, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.dirname(os.path.dirname(HERE))
IMG_DIR = os.path.join(REPO, "assets/images/nbme/micro")
OUT = os.path.join(REPO, "assets/js/nbme/micro-data.js")

SECTIONS = [
    "s01_gpc", "s02_gpr", "s03_gnc_resp", "s04_enteric", "s05_zoonotic_spiro",
    "s06_intracellular", "s07_myco_misc", "s08_abx", "s09_bact_general",
    "s10_herpes_dna", "s11_rna", "s12_hiv_hep", "s13_fungi", "s14_protozoa",
    "s15_helminths", "s16_systems", "s17_extra",
]
# New sections are picked up automatically: any file named n##_*.py
EXTRA_GLOB = "n"
LENGTH_CUE_RATIO = 1.15   # key may not exceed the longest distractor by more than 15%
STRICT = "--strict" in sys.argv

def main():
    import qcore
    questions = []
    sections = SECTIONS + sorted(f[:-3] for f in os.listdir(HERE) if f.startswith(EXTRA_GLOB) and f[1:3].isdigit() and f.endswith(".py"))
    try:
        from retro import RETRO
    except ImportError:
        RETRO = {}
    for s in sections:
        if not os.path.exists(os.path.join(HERE, s + ".py")):
            print("  (missing section", s, ")"); continue
        mod = importlib.import_module(s)
        for q in mod.QUESTIONS:
            r = RETRO.get(q["topic"])
            if r:
                q["opts"] = list(q["opts"])
                q["_pre_opts"] = list(q["opts"])
                if "c" in r: q["opts"][0] = r["c"]
                for prefix, text in (r.get("o") or {}).items():
                    hits = [k for k in range(1, 5) if q["opts"][k].lower().startswith(prefix.lower())]
                    if len(hits) != 1: print(f"  retro {q['topic']!r}: option prefix {prefix!r} matched {len(hits)}")
                    else: q["opts"][hits[0]] = text
                if "e" in r: q["expl"] = r["e"]
                if "d" in r: q["difficulty"] = r["d"]
                if "why" in r and not q.get("why"): q["why"] = r["why"]
                if "table" in r:
                    t = r["table"]; q["tables"] = q["tables"] + ([t] if isinstance(t, dict) else list(t))
                r["_used"] = True
            questions.append(q)
    for k, r in RETRO.items():
        if not r.get("_used"): print("  retro topic not matched:", k)

    errors, out, length_cues = [], [], []
    seen_stems = set()
    for i, q in enumerate(questions):
        qid = 3001 + i
        opts = q["opts"]
        if len(opts) != 5: errors.append(f"{qid} {q['topic']}: {len(opts)} options")
        if len(set(o.strip().lower() for o in opts)) != len(opts): errors.append(f"{qid} {q['topic']}: duplicate option")
        key = q["stem"][:80]
        if key in seen_stems: errors.append(f"{qid}: duplicate stem {key!r}")
        seen_stems.add(key)
        for im in q.get("images") or []:
            if not os.path.exists(os.path.join(IMG_DIR, im)): errors.append(f"{qid}: missing image {im}")
        rng = random.Random(qid * 7919)
        order = list(range(5)); rng.shuffle(order)
        letters = "ABCDE"
        options = {letters[pos]: opts[src] for pos, src in enumerate(order)}
        answer = letters[order.index(0)]
        wrong = {}
        why = q.get("why")
        if isinstance(why, list):
            if len(why) != 4: errors.append(f"{qid} {q['topic']}: why has {len(why)} items")
            for k, reason in enumerate(why[:4]): wrong[k + 1] = reason
        elif isinstance(why, dict):
            pre = q.get("_pre_opts") or opts
            for prefix, reason in why.items():
                p = prefix.lower()
                hits = [k for k in range(1, 5) if opts[k].lower().startswith(p)]
                if len(hits) != 1:
                    hits = [k for k in range(1, 5) if pre[k].lower().startswith(p)]
                if len(hits) != 1: errors.append(f"{qid} {q['topic']}: why prefix {prefix!r} matched {len(hits)}")
                else: wrong[hits[0]] = reason
        key_len, max_other = len(opts[0]), max(len(o) for o in opts[1:])
        if key_len > max_other * LENGTH_CUE_RATIO and key_len - max_other > 10:
            length_cues.append(f"{qid} {q['topic']}: key {key_len} vs longest distractor {max_other}")
        diff = q.get("difficulty", "medium")
        if diff not in ("easy", "medium", "hard"): errors.append(f"{qid}: bad difficulty {diff}")
        item = {"id": qid, "part": q["tag"], "tag": q["tag"], "difficulty": diff,
                "topic": q["topic"], "stem": q["stem"], "options": options, "answer": answer,
                "explanation": q["expl"]}
        if q.get("images"): item["images"] = q["images"]
        if wrong: item["wrong"] = {letters[order.index(k)]: v for k, v in wrong.items()}
        for t in q.get("tables") or []:
            if not isinstance(t, dict) or "cols" not in t:
                errors.append(f"{qid} {q['topic']}: bad table value {str(t)[:40]!r} (name collision with a tag constant?)")
            elif any(len(r) != len(t["cols"]) for r in t["rows"]):
                errors.append(f"{qid}: table {t['title']!r} row width mismatch")
        if q.get("tables"): item["tables"] = [{k: v for k, v in t.items() if v or k != "highlight"} for t in q["tables"]]
        out.append(item)

    key_longest = sum(1 for q in questions if len(q["opts"][0]) > max(len(o) for o in q["opts"][1:]))
    print(f"key strictly longest: {key_longest}/{len(questions)} ({100*key_longest//max(1,len(questions))}%) — target ≈20%")
    if length_cues:
        print(f"LENGTH CUES ({len(length_cues)}):"); [print(" ", c) for c in length_cues]
        if STRICT: errors.append(f"{len(length_cues)} length cues")
    if errors:
        print("ERRORS:"); [print(" ", e) for e in errors]; sys.exit(1)

    credits_path = os.path.join(HERE, "..", "credits.json")
    credits = json.load(open(credits_path)) if os.path.exists(credits_path) else {}
    used = sorted({im for q in out for im in q.get("images", [])})
    image_credits = [dict(file=f, **credits[f]) for f in used if f in credits]

    data = {
        "setTitle": "Step 1 Microbiology: Bacteria, Viruses, Fungi & Parasites",
        "setSubtitle": "NBME-style review of every high-yield organism — clinical presentation, virulence and molecular mechanisms, diagnosis, treatment and drug mechanisms, and epidemiology — with gross, micro and culture images.",
        "imageBase": "/assets/images/nbme/micro/",
        "imageCredits": image_credits,
        "questions": out,
    }
    with open(OUT, "w") as f:
        f.write("window.NBME_MICRO_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

    tags = collections.Counter(q["tag"] for q in out)
    print(f"{len(out)} questions, {sum(1 for q in out if q.get('images'))} with images, {len(used)} images")
    for t, n in sorted(tags.items()): print(f"  {n:4d}  {t}")
    print("difficulty:", dict(collections.Counter(q["difficulty"] for q in out)))
    print("with why:", sum(1 for q in out if q.get("wrong")), " full why:", sum(1 for q in out if len(q.get("wrong", {})) == 4), " with tables:", sum(1 for q in out if q.get("tables")))
    print("answer spread:", dict(sorted(collections.Counter(q['answer'] for q in out).items())))
    unused = set(os.listdir(IMG_DIR)) - set(used) if os.path.isdir(IMG_DIR) else set()
    if unused: print("unused images:", sorted(unused))

if __name__ == "__main__":
    main()
