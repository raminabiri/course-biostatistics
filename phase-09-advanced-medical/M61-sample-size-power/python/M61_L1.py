from csv import DictReader
from math import ceil
from pathlib import Path
from statistics import NormalDist

n = NormalDist()
with (Path(__file__).resolve().parents[1]/"data/M61_design.csv").open() as f:
    rows = list(DictReader(f))
out = []
for r in rows:
    delta, sd, alpha, power = (float(r[k]) for k in ("difference","sd","alpha","power"))
    size = 2*(n.inv_cdf(1-alpha/2)+n.inv_cdf(power))**2*(sd/delta)**2
    print(size,ceil(size))
    out.append(ceil(size))
assert out==[63,175]
