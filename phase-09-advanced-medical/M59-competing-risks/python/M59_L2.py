from collections import defaultdict
from csv import DictReader
from pathlib import Path

groups = defaultdict(list)
with (Path(__file__).resolve().parents[1]/"data/M59_groups.csv").open() as f:
    for row in DictReader(f):
        groups[row["group"]].append((int(row["time"]),int(row["status"])))
out = {}
for name, rows in sorted(groups.items()):
    survival,cif = 1,0
    for time in sorted({t for t,s in rows if s and t<=4}):
        risk = sum(t>=time for t,_ in rows)
        counts = [sum(t==time and s==code for t,s in rows) for code in (1,2)]
        cif += survival*counts[0]/risk
        survival *= 1-sum(counts)/risk
    out[name] = cif
print(out,out["B"]-out["A"])
assert abs(out["A"]-13/60)<1e-10 and abs(out["B"]-.3)<1e-10
