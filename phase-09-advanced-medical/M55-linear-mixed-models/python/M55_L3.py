from collections import defaultdict
from csv import DictReader
from math import isclose, sqrt
from pathlib import Path
from statistics import mean, variance

classes = defaultdict(list)
with (Path(__file__).resolve().parents[1] / "data/M55_clusters.csv").open() as f:
    for row in DictReader(f):
        classes[row["group"],row["class_id"]].append(float(row["y"]))
assert all(len(values)==3 for values in classes.values())
means = defaultdict(list)
for (group,_),values in classes.items():
    means[group].append(mean(values))
difference = mean(means["B"])-mean(means["A"])
se = sqrt(sum(variance(v)/len(v) for v in means.values()))
print(difference,se)
assert difference==2 and isclose(se,sqrt(8))
