from csv import DictReader
from math import exp, log
from pathlib import Path
from statistics import NormalDist

with (Path(__file__).resolve().parents[1] / "data/M53_probit.csv").open() as f:
    rows = list(DictReader(f))
x = [log(float(row["input"])) for row in rows]
y = [NormalDist().inv_cdf(int(row["positive"])/int(row["total"])) for row in rows]
slope = (y[-1]-y[0])/(x[-1]-x[0])
intercept = y[0]-slope*x[0]
x50 = exp(-intercept/slope)
print(intercept, slope, x50)
assert abs(x50-2)<1e-8
