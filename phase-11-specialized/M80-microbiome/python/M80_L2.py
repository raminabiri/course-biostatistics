import csv
from itertools import combinations
from statistics import mean
from math import isclose
with open("data/M80_L2.csv") as f:
    rows=list(csv.DictReader(f))
p=[int(r["t1"])/(int(r["t1"])+int(r["t2"])) for r in rows]
total=sum((x-mean(p))**2 for x in p)
def score(indices):
    a=[x for i,x in enumerate(p) if i in indices]
    b=[x for i,x in enumerate(p) if i not in indices]
    within=sum((x-mean(g))**2 for g in (a,b) for x in g)
    return (total-within)/(within/4)
observed=score(tuple(i for i,r in enumerate(rows) if r["group"]=="A"))
null=[score(i) for i in combinations(range(len(rows)),3)]
prob=mean(x>=observed-1e-10 for x in null)
assert isclose(observed,54) and prob==.1
print(observed,prob)
