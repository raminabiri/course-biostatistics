import csv
from statistics import mean,linear_regression
from math import isclose
with open("data/P03.csv") as f:
    data=[(int(r["dose"]),float(r["signal"])) for r in csv.DictReader(f)]
groups=[[y for x,y in data if x==g] for g in range(3)]
overall=mean(y for _,y in data)
between=sum(len(g)*(mean(g)-overall)**2 for g in groups)
within=sum((y-mean(g))**2 for g in groups for y in g)
f=(between/2)/(within/21)
slope=linear_regression(*zip(*data)).slope
assert isclose(f,32) and isclose(slope,4)
print(f,slope)
