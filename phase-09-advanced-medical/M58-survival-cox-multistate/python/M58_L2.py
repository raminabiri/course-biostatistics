from csv import DictReader
from math import exp
from pathlib import Path
with (Path(__file__).resolve().parents[1]/"data/M58_cox.csv").open() as f:
    rows = [(x["group"],int(x["time"]),int(x["event"])) for x in DictReader(f)]
weight = exp(-.7322549871133526)
results = []
for group,time in sorted(((g,t) for g,t,e in rows if e),key=lambda v:v[1]):
    a = sum(g=="A" and t>=time for g,t,_ in rows)
    b = sum(g=="B" and t>=time for g,t,_ in rows)
    result = (group=="B")-b*weight/(a+b*weight)
    results.append(result)
    print(time,result)
assert abs(results[0]+.3247001)<1e-6
