from csv import DictReader
from pathlib import Path

def curve(x, low=10, high=90, mid=2, slope=1.5, shape=1):
    return low+(high-low)/(1+(mid/x)**slope)**shape

with (Path(__file__).resolve().parents[1] / "data/M53_curve.csv").open() as f:
    rows = list(DictReader(f))
sse = sum((float(row["observed"])-curve(float(row["input"])))**2 for row in rows)
print(curve(2), curve(2, shape=2), sse)
assert curve(2)==50 and curve(2,shape=2)==30
