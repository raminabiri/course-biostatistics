import csv
from pathlib import Path
from math import isclose, sqrt
from statistics import mean, median, variance, stdev

path = Path(__file__).resolve().parents[1] / "data" / "M05_module.csv"
with path.open(newline="") as stream:
    rows = list(csv.DictReader(stream))
x = [int(row["wait"]) for row in rows]
y = [int(row["replacement"]) for row in rows]
result = (mean(x), median(x), mean(y), median(y), max(x)-min(x),
          variance(x), stdev(x), stdev(x)/sqrt(len(x)))
assert all(isclose(a,b) for a,b in zip(result,(14,14,18,14,8,10,sqrt(10),sqrt(2))))
for key,value in zip(("mean","median","mean_after","median_after","range","variance","sd","se"),result):
    print(key,value)
