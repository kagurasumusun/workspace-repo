#!/usr/bin/env python3
"""Conservative deterministic candidate prefilter; final routing remains semantic."""
import json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[2]
registry=root/"skill-router"/"routing-registry.json"
task=" ".join(sys.argv[1:]).lower()
data=json.loads(registry.read_text(encoding="utf-8"))
c=[]
for s in data.get("skills",[]):
    hits=sum(1 for k in s.get("keywords",[]) if k.lower() in task)
    excluded=any(x.lower() in task for x in s.get("excludes",[]))
    if hits and not excluded: c.append((hits,s["name"]))
c.sort(reverse=True)
print(json.dumps({"decision":"use" if c else "abstain","candidates":[n for _,n in c[:3]],"note":"prefilter only; perform semantic applicability check before activation"},ensure_ascii=False,indent=2))
