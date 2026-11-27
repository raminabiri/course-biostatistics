from collections import defaultdict
from csv import DictReader
from math import isclose
from pathlib import Path

groups = defaultdict(list)
with (Path(__file__).resolve().parents[1] / "data/M57_time.csv").open() as f:
    for row in DictReader(f):
        groups[row["group"]].append((int(row["time"]), int(row["event"])))
results = []
for group, rows in sorted(groups.items()):
    survival = 1.0
    for time in sorted({t for t,event in rows if event}):
        risk = sum(t>=time for t,_ in rows)
        events = sum(t==time and event for t,event in rows)
        survival *= 1-events/risk
        results.append(survival)
        print(group,time,risk,events,survival)
assert all(isclose(a,b) for a,b in zip(results,(.8,8/15,4/15,.8,.4)))
