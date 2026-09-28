import sys, importlib
sys.path.insert(0,'.')
mod=importlib.import_module(sys.argv[1])
only_flagged = "-a" not in sys.argv
for q in mod.QUESTIONS:
    o=q["opts"]; mx=max(len(x) for x in o[1:]); flagged = len(o[0])>mx*1.15 and len(o[0])-mx>10
    if only_flagged and not flagged: continue
    print(f"[{q['topic']}]")
    for i,x in enumerate(o): print(f"   {'*' if i==0 else '-'}{len(x):3d} {x}")
