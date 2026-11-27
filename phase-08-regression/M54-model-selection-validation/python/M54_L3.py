from csv import DictReader
from math import copysign
from pathlib import Path

with (Path(__file__).resolve().parents[1] / "data/M54_penalty.csv").open() as f:
    pairs = [(float(r["x"]),float(r["y"])) for r in DictReader(f)]
xx = sum(x*x for x,y in pairs)
xy = sum(x*y for x,y in pairs)
for penalty in (0,5,10,20):
    ridge = xy/(xx+penalty)
    lasso = copysign(max(0,abs(xy)-penalty),xy)/xx
    print(penalty,ridge,lasso)
assert lasso==0 and abs(ridge-2/3)<1e-12
