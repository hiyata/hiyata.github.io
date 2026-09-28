"""Overlay for the original 392 questions: difficulty, rebalanced options, distractor explanations, tables.
retro_s*.py define entries; retro_z*.py are later passes that merge into (and override) them.
Keys: d=difficulty, c=new correct text, o={distractor prefix: new text}, why={prefix: reason}, table=..., e=new explanation."""
import importlib, os
RETRO = {}
_here = os.path.dirname(os.path.abspath(__file__))
for f in sorted(os.listdir(_here)):
    if not (f.startswith("retro_") and f.endswith(".py")):
        continue
    m = importlib.import_module(f[:-3])
    second_pass = f.startswith("retro_z")
    for k, v in m.R.items():
        if k in RETRO:
            if not second_pass:
                raise SystemExit(f"duplicate retro topic in {f}: {k}")
            merged = dict(RETRO[k])
            for kk, vv in v.items():
                if kk == "o":
                    merged["o"] = {**merged.get("o", {}), **vv}
                else:
                    merged[kk] = vv
            RETRO[k] = merged
        else:
            RETRO[k] = v
