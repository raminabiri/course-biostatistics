from collections import Counter
from csv import DictReader
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
from scipy.stats import chi2

with (Path(__file__).resolve().parents[1] / "data/M38_practice.csv").open() as f:
    rows = list(DictReader(f))
assert len(rows) == len({r["id"] for r in rows}) == 240
count = Counter((r["stratum"], r["group"], r["success"]) for r in rows)
tables = np.array([[count[stratum, group, success]
                    for group in ("A", "B") for success in ("1", "0")]
                   for stratum in ("easy", "hard")])
a, b, c, d = tables.T
n = tables.sum(axis=1)
r, m = a+b, a+c
print("L1:", a/r, c/(c+d), a.sum()/r.sum(), c.sum()/(c+d).sum())
theta = sum(a*d/n)/sum(b*c/n)
expected = r*m/n
variance = r*(n-r)*m*(n-m)/(n*n*(n-1))
cmh = sum(a-expected)**2/sum(variance)
print("L2:",theta,cmh,chi2.sf(cmh,1))
bd = 0
for observed, row, column, total in zip(a,r,m,n):
    def equation(x):
        return x*(total-row-column+x)-theta*(row-x)*(column-x)

    x = brentq(equation,max(0,row+column-total),min(row,column))
    fitted = np.array([x,row-x,column-x,total-row-column+x])
    bd += (observed-x)**2*sum(1/fitted)
print("L3:",bd,chi2.sf(bd,len(a)-1))
assert np.isclose(theta,.7260273973) and np.isclose(bd,.2124803146)
