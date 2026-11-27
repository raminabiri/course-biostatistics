from collections import defaultdict
from csv import DictReader
from math import isclose
from pathlib import Path
from statistics import mean, variance

groups = defaultdict(list)
with (Path(__file__).resolve().parents[1] / "data/M55_repeated.csv").open() as f:
    for row in DictReader(f):
        groups[row["id"]].append((int(row["time"]),float(row["y"])))
assert all(sorted(t for t,y in rows)==[0,1,2] for rows in groups.values())
levels = {key:mean(y for _,y in rows) for key,rows in groups.items()}
pairs = [(t-1,y-levels[key]) for key,rows in groups.items() for t,y in rows]
slope = sum(t*y for t,y in pairs)/sum(t*t for t,y in pairs)
error = sum((y-slope*t)**2 for t,y in pairs)/(len(pairs)-len(groups)-1)
random_intercept = variance(levels.values())-error/3
print(mean(levels.values())-slope,slope,random_intercept,error)
assert isclose(slope,23/12) and isclose(error,.3560606060606061)
