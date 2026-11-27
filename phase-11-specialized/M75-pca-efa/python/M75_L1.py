import csv
from math import sqrt, isclose
from statistics import mean, stdev, correlation
with open("data/M75_L1.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
x = [float(r["fatigue"]) for r in rows]
y = [float(r["activity"]) for r in rows]
r = correlation(x,y)
def scale(values):
    m, sd = mean(values), stdev(values)
    return [(v-m)/sd for v in values]
scores = [(a+b)/sqrt(2) for a,b in zip(scale(x),scale(y))]
assert isclose(r,1/sqrt(2)) and isclose(stdev(scores)**2,1+r)
print(1+r,1-r,(1+r)/2,scores)
