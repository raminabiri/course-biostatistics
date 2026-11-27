import csv
from math import dist,isclose
from statistics import mean
with open("data/M77_L1.csv") as f:
    points=[(float(r["x"]),float(r["y"])) for r in csv.DictReader(f)]
a,b=points[:2],points[2:]
centers=[tuple(map(mean,zip(*g))) for g in (a,b)]
score=sum(dist(p,c)**2 for g,c in zip((a,b),centers) for p in g)
height=max(dist(p,q) for p in a for q in b)
assert score==4 and isclose(height,164**.5)
print(centers,score,height)
