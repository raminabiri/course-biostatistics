from csv import DictReader
from math import erfc, sqrt
from pathlib import Path

with (Path(__file__).resolve().parents[1]/"data/M57_time.csv").open() as f:
    rows = [(r["group"],int(r["time"]),int(r["event"])) for r in DictReader(f)]
observed = expected = variance = 0.0
for time in sorted({t for _,t,e in rows if e}):
    risk = sum(t>=time for _,t,_ in rows)
    risk_a = sum(g=="A" and t>=time for g,t,_ in rows)
    events = sum(t==time and e for _,t,e in rows)
    observed += sum(g=="A" and t==time and e for g,t,e in rows)
    p = risk_a/risk
    expected += events*p
    if risk>1:
        variance += events*p*(1-p)*(risk-events)/(risk-1)
statistic = (observed-expected)**2/variance
print(observed,expected,variance,statistic,erfc(sqrt(statistic/2)))
assert abs(statistic-.663)<.001
