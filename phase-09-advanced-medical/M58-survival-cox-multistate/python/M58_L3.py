from collections import defaultdict
from csv import DictReader
from pathlib import Path
groups = defaultdict(list)
with (Path(__file__).resolve().parents[1]/"data/M58_cox.csv").open() as f:
    for row in DictReader(f):
        groups[row["group"]].append((int(row["time"]),int(row["event"])))

def rmst(rows, tau):
    area, previous, survival = 0, 0, 1
    for t in sorted({t for t,e in rows if e and t<tau}):
        area += (t-previous)*survival
        survival *= 1-sum(w==t and e for w,e in rows)/sum(w>=t for w,_ in rows)
        previous = t
    return area+(tau-previous)*survival

out = {g:rmst(rows,5) for g,rows in groups.items()}
print(out,out["B"]-out["A"])
assert abs(out["A"]-3.4)<1e-10 and abs(out["B"]-4.4)<1e-10
