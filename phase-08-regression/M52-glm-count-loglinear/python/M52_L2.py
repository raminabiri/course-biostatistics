from csv import DictReader
from math import exp
from pathlib import Path
from statistics import mean, variance

with (Path(__file__).resolve().parents[1] / "data/M52_counts.csv").open() as f:
    x = [int(row["events"]) for row in DictReader(f)]
mu, v = mean(x), variance(x)
p0 = exp(-2)
print(mu, v, mu**2/(v-mu), x.count(0)/len(x), p0, .25+.75*p0, .25, 2*p0/(1-p0))
assert mu == 2 and x.count(0) == 4
