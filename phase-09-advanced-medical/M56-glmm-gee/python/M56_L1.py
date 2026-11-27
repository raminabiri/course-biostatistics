from collections import defaultdict
from csv import DictReader
from math import isclose, sqrt
from pathlib import Path

groups = defaultdict(lambda: defaultdict(list))
with (Path(__file__).resolve().parents[1] / "data/M56_binary.csv").open() as f:
    for row in DictReader(f):
        groups[row["group"]][row["id"]].append(int(row["completed"]))
odds = {}
variance = {}
for group, people in groups.items():
    n = sum(map(len, people.values()))
    p = sum(sum(values) for values in people.values()) / n
    scores = [sum(values) - len(values)*p for values in people.values()]
    odds[group] = p/(1-p)
    variance[group] = sum(s*s for s in scores)/(n*p*(1-p))**2
result = odds["B"]/odds["A"]
print(result,sqrt(sum(variance.values())))
assert isclose(result,10/3)
