import csv
from statistics import linear_regression
from math import isclose
with open("data/M73_L1.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
fit = linear_regression([float(r["x"]) for r in rows], [float(r["signal"]) for r in rows])
unknown = (12.5-fit.intercept)/fit.slope
lod, loq = (k*.3/fit.slope for k in (3.3,10))
assert all(isclose(a,b) for a,b in zip((unknown,lod,loq),(3.5,.33,1)))
print(fit.slope, unknown, lod, loq)
