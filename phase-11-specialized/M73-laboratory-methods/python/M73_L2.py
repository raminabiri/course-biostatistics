import csv
from math import log, isclose
from statistics import linear_regression
with open("data/M73_L2.csv", newline="") as stream:
    rows = [(float(r["hour"]),float(r["conc"])) for r in csv.DictReader(stream)]
area = sum((t2-t1)*(c1+c2)/2 for (t1,c1),(t2,c2) in zip(rows,rows[1:]))
time, peak = max(rows,key=lambda row:row[1])
terminal = [(t,log(c)) for t,c in rows if t>=2 and c>0]
slope = linear_regression(*zip(*terminal)).slope
half_life = -log(2)/slope
assert (area,peak,time)==(14.5,8,1) and isclose(half_life,1)
print(area,peak,time,half_life)
