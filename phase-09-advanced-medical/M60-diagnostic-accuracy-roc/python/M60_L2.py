from csv import DictReader
from math import erfc, sqrt
from pathlib import Path
from statistics import mean, variance

with (Path(__file__).resolve().parents[1]/"data/M60_roc.csv").open() as f:
    rows = sorted(DictReader(f),key=lambda r:int(r["id"]))

def placements(key):
    p,n = [[float(r[key]) for r in rows if r["reference"]==label] for label in ("1","0")]
    matrix = [[(a>b)+.5*(a==b) for b in n] for a in p]
    return list(map(mean,matrix)),list(map(mean,zip(*matrix)))

a,b = map(placements,("score_a","score_b"))
auc_a,auc_b = mean(a[0]),mean(b[0])
v = sum(variance([y-x for x,y in zip(u,w)])/len(u) for u,w in zip(a,b))
z = (auc_b-auc_a)/sqrt(v)
print(auc_a,auc_b,v,z,erfc(abs(z)/sqrt(2)))
assert abs(v-.0048)<1e-10
