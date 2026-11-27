from collections import defaultdict, Counter
from csv import DictReader
from pathlib import Path
from statistics import mean

observed = defaultdict(list)
missing = Counter()
with (Path(__file__).resolve().parents[1]/"data/M62_missing.csv").open() as f:
    for row in DictReader(f):
        group = row["group"]
        if row["y"] == "":
            missing[group] += 1
        else:
            observed[group].append(float(row["y"]))
complete = mean(y for values in observed.values() for y in values)
weighted = mean(map(mean,observed.values()))
print(missing,complete,weighted)
assert missing=={"A":1,"B":4} and abs(complete-104/7)<1e-9 and weighted==17
