import csv
from math import log2
from pathlib import Path
from statistics import quantiles

path = Path(__file__).resolve().parents[1] / "data" / "M06_module.csv"
with path.open(newline="") as stream:
    x = [int(row["wait"]) for row in csv.DictReader(stream)]
q1, median, q3 = quantiles(x, n=4, method="inclusive")
width = q3-q1
low, high = q1-1.5*width, q3+1.5*width
flagged = [v for v in x if v<low or v>high]
assert (q1,median,q3,low,high,flagged)==(3,5,7,-3,13,[40])
print(q1,median,q3,width,low,high,flagged,log2(40/8))
