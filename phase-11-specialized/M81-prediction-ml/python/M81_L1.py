import csv
from math import isclose
from statistics import mean
with open("data/M81_L1.csv") as f:
    rows=[(float(r["p"]),int(r["y"])) for r in csv.DictReader(f)]
score=mean((p-y)**2 for p,y in rows)
auc=mean((a>b)+.5*(a==b) for a,ya in rows if ya==1 for b,yb in rows if yb==0)
assert isclose(score,.325) and auc==.75
print(score,auc)
