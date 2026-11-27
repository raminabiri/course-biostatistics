from csv import DictReader
from math import exp
from pathlib import Path

with (Path(__file__).resolve().parents[1]/"data/M58_cox.csv").open() as f:
    rows = [(r["group"],int(r["time"]),int(r["event"])) for r in DictReader(f)]
events = [(g,t) for g,t,e in rows if e]
assert len({t for _,t in events})==len(events)
risk_sets = []
for group,time in events:
    risk = [g for g,t,_ in rows if t>=time]
    risk_sets.append((int(group=="B"),risk.count("A"),risk.count("B")))
def score(beta):
    weight = exp(beta)
    return sum(observed-b*weight/(a+b*weight) for observed,a,b in risk_sets)
lo,hi = -20,20
assert score(lo)>0>score(hi)
for _ in range(70):
    mid = (lo+hi)/2
    if score(mid)>0:
        lo=mid
    else:
        hi=mid
beta=(lo+hi)/2
print(beta,exp(beta))
assert abs(exp(beta)-.4808235)<1e-6
