from csv import DictReader
from math import erfc, sqrt
from pathlib import Path
with (Path(__file__).resolve().parents[1]/"data/M57_time.csv").open() as f:
    rows = [(r["group"],int(r["time"]),int(r["event"])) for r in DictReader(f)]
risk_sets = []
for time in sorted({t for _,t,e in rows if e}):
    risk = [g for g,t,_ in rows if t>=time]
    events = [g for g,t,e in rows if t==time and e]
    n,k = len(risk),len(events)
    p = risk.count("A")/n
    variance = k*p*(1-p)*(n-k)/(n-1) if n>1 else 0
    risk_sets.append((n,events.count("A")-k*p,variance))
for method, weight in (("logrank",lambda n:1),("breslow",lambda n:n),("tarone",sqrt)):
    u = sum(weight(n)*difference for n,difference,v in risk_sets)
    variance = sum(weight(n)**2*v for n,difference,v in risk_sets)
    stat = u*u/variance
    print(method,stat,erfc(sqrt(stat/2)))
    if method=="logrank":
        assert abs(stat-.663280189)<1e-8
