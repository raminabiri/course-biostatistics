from collections import defaultdict
from csv import DictReader
from math import isclose, sqrt
from pathlib import Path

groups = defaultdict(lambda: defaultdict(lambda: [0, 0]))
with (Path(__file__).resolve().parents[1] / "data/M56_counts.csv").open() as f:
    for row in DictReader(f):
        values = groups[row["group"]][row["id"]]
        values[0] += int(row["events"])
        values[1] += int(row["exposure"])
rates = {}
variances = []
for group, people in groups.items():
    events, exposure = map(sum, zip(*people.values()))
    rate = rates[group] = events/exposure
    variances.append(sum((y-rate*t)**2 for y,t in people.values())/events**2)
ratio, se = rates["B"]/rates["A"], sqrt(sum(variances))
print(ratio, se)
assert ratio==2 and isclose(se,sqrt(10/144+20/576))
