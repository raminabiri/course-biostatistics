from csv import DictReader
from pathlib import Path

with (Path(__file__).resolve().parents[1]/"data/M59_events.csv").open() as f:
    rows = [(int(r["time"]),int(r["status"])) for r in DictReader(f)]
survival, target, competing = 1,0,0
for time in sorted({t for t,s in rows if s}):
    risk = sum(t>=time for t,_ in rows)
    event1 = sum(t==time and s==1 for t,s in rows)
    event2 = sum(t==time and s==2 for t,s in rows)
    target += survival*event1/risk
    competing += survival*event2/risk
    survival *= 1-(event1+event2)/risk
    print(time,risk,survival,target,competing)
assert abs(target-13/60)<1e-10 and abs(survival+target+competing-1)<1e-10
