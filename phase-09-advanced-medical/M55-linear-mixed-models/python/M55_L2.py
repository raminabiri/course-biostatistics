from collections import defaultdict
from csv import DictReader
from math import isclose
from pathlib import Path
from statistics import mean, variance

groups = defaultdict(dict)
with (Path(__file__).resolve().parents[1] / "data/M55_repeated.csv").open() as f:
    for row in DictReader(f):
        groups[row["id"]][int(row["time"])] = float(row["y"])
slopes = [(v[2]-v[0])/2 for v in groups.values()]
slope = mean(slopes)
error = sum((y-mean(v.values())-slope*(t-1))**2
            for v in groups.values() for t,y in v.items())/(3*len(groups)-len(groups)-1)
print(slopes, slope, variance(slopes), error/2)
assert isclose(slope,23/12) and variance(slopes)<error/2
