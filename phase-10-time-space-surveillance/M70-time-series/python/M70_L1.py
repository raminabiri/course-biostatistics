import csv
from statistics import linear_regression
with open("data/M70_L1.csv", newline="") as stream:
    rows = [{k:int(v) for k,v in row.items()} for row in csv.DictReader(stream)]
def line(post):
    group = [r for r in rows if r["post"] == post]
    return linear_regression([r["month"] for r in group], [r["wait"] for r in group])
before, after = line(0), line(1)
step = (after.intercept + 7*after.slope) - (before.intercept + 7*before.slope)
slope_change = after.slope-before.slope
assert abs(step+5)<1e-10 and abs(slope_change+2)<1e-10
print(before.slope, step, slope_change, step+3*slope_change)
