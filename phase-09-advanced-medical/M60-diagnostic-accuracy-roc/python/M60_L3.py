from csv import DictReader
from pathlib import Path
from statistics import mean

with (Path(__file__).resolve().parents[1]/"data/M60_roc.csv").open() as f:
    rows = [(int(r["reference"]),float(r["score_a"]),float(r["score_b"])) for r in DictReader(f)]

def gap(fn):
    return mean(fn(a,b) for y,a,b in rows if y==1)-mean(fn(a,b) for y,a,b in rows if y==0)
out = gap(lambda a,b:(b>=.6)-(a>=.6)),gap(lambda a,b:b-a)
print(out)
assert all(abs(a-b)<1e-10 for a,b in zip(out,(.4,.026)))
