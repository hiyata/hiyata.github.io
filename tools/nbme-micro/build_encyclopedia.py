"""Assemble the microbiology encyclopedia into assets/js/nbme/micro-encyclopedia.js.

Each e##_*.py file defines ENTRIES = [E(...), ...]. The build checks that ids are
unique, that every image is present and credited, and that every entry has a
high-yield layer, then writes one JS file the exam page loads alongside the bank.
"""
import importlib, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.dirname(os.path.dirname(HERE))
IMG_DIR = os.path.join(REPO, "assets/images/nbme/micro")
OUT = os.path.join(REPO, "assets/js/nbme/micro-encyclopedia.js")

# Display order of the groups in the sidebar.
GROUP_ORDER = [
    "Gram-Positive Cocci",
    "Gram-Positive Rods",
    "Gram-Negative Cocci",
    "Gram-Negative Rods",
    "Enteric Gram-Negative Rods",
    "Spirochetes",
    "Mycobacteria",
    "Intracellular & Atypical Bacteria",
    "DNA Viruses",
    "RNA Viruses",
    "Hepatitis Viruses",
    "Fungi",
    "Protozoa",
    "Helminths",
    "Principles & Pharmacology",
]


def main():
    entries, errors = [], []
    files = sorted(f[:-3] for f in os.listdir(HERE)
                   if f.startswith("e") and f[1:3].isdigit() and f.endswith(".py"))
    if not files:
        sys.exit("no e##_*.py encyclopedia files found")
    for mod_name in files:
        mod = importlib.import_module(mod_name)
        for e in mod.ENTRIES:
            e["_src"] = mod_name
            entries.append(e)

    credits = json.load(open(os.path.join(HERE, "credits.json")))
    seen = {}
    for e in entries:
        if e["id"] in seen:
            errors.append(f"duplicate id {e['id']} ({e['_src']} and {seen[e['id']]})")
        seen[e["id"]] = e["_src"]
        if e["group"] not in GROUP_ORDER:
            errors.append(f"{e['id']}: unknown group {e['group']!r}")
        if not e["sections"]:
            errors.append(f"{e['id']}: no sections")
        hy = sum(1 for s in e["sections"] for p in s["p"] if p["hy"])
        if hy == 0:
            errors.append(f"{e['id']}: no high-yield paragraphs")
        for f, _cap in e["images"]:
            if not os.path.exists(os.path.join(IMG_DIR, f)):
                errors.append(f"{e['id']}: missing image {f}")
            elif f not in credits:
                errors.append(f"{e['id']}: no credit recorded for {f}")
        for r in e.get("research", {}).get("reviews", []):
            if not r["url"].startswith(("http://", "https://")):
                errors.append(f"{e['id']}: review {r['title']!r} has a non-url link {r['url']!r}")
        for tl in e.get("history", {}).get("timeline", []):
            f = tl.get("img")
            if not f:
                continue
            if not os.path.exists(os.path.join(IMG_DIR, f)):
                errors.append(f"{e['id']}: missing timeline image {f}")
            elif f not in credits:
                errors.append(f"{e['id']}: no credit recorded for timeline image {f}")

    if errors:
        print("ERRORS:")
        for x in errors:
            print("  ", x)
        sys.exit(1)

    order = {g: i for i, g in enumerate(GROUP_ORDER)}
    entries.sort(key=lambda e: (order[e["group"]], e["name"]))
    for e in entries:
        e.pop("_src", None)

    used = sorted({f for e in entries for f, _ in e["images"]} |
                  {tl["img"] for e in entries for tl in e.get("history", {}).get("timeline", []) if tl.get("img")})
    data = {
        "title": "Microbiology Encyclopedia",
        "subtitle": "Every organism in the bank: the science of how it works, with the Step 1 high-yield layer marked.",
        "imageBase": "/assets/images/nbme/micro/",
        "groups": [g for g in GROUP_ORDER if any(e["group"] == g for e in entries)],
        "imageCredits": [dict(file=f, **credits[f]) for f in used if f in credits],
        "entries": entries,
    }
    with open(OUT, "w") as fh:
        fh.write("window.NBME_MICRO_ENCYCLOPEDIA = " + json.dumps(data, indent=1, ensure_ascii=False) + ";\n")

    paras = sum(len(s["p"]) for e in entries for s in e["sections"])
    hy = sum(1 for e in entries for s in e["sections"] for p in s["p"] if p["hy"])
    words = sum(len(p["t"].split()) for e in entries for s in e["sections"] for p in s["p"])
    print(f"{len(entries)} entries, {paras} paragraphs ({hy} high-yield, {100*hy//max(1,paras)}%), "
          f"~{words:,} words, {len(used)} images")
    by = collections.Counter(e["group"] for e in entries)
    for g in data["groups"]:
        print(f"  {by[g]:3d}  {g}")
    print(f"written to {os.path.relpath(OUT, REPO)}  ({os.path.getsize(OUT)//1024} KB)")


if __name__ == "__main__":
    main()
