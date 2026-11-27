from csv import DictReader
from math import sqrt
from pathlib import Path
from statistics import mean

with (Path(__file__).resolve().parents[1] / "data/M54_cv.csv").open() as f:
    rows = [tuple(int(row[k]) for k in ("fold","x","y")) for row in DictReader(f)]
errors = [], []
for fold in sorted({r[0] for r in rows}):
    train = [(x,y) for f,x,y in rows if f!=fold]
    xbar, ybar = map(mean,zip(*train))
    slope = sum((x-xbar)*(y-ybar) for x,y in train)/sum((x-xbar)**2 for x,y in train)
    for f,x,y in rows:
        if f==fold:
            errors[0].append((y-ybar)**2)
            errors[1].append((y-ybar-slope*(x-xbar))**2)
out = [sqrt(mean(e)) for e in errors]
print(out)
assert len(errors[0])==9 and out[1]<out[0]
