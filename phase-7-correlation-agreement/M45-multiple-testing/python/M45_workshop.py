from csv import DictReader
from math import expm1, log1p
from pathlib import Path

import numpy as np

with (Path(__file__).resolve().parents[1] / "data/M45_pvalues.csv").open() as f:
    rows = sorted(DictReader(f),key=lambda row:float(row["p_raw"]))
p = np.array([float(row["p_raw"]) for row in rows])
m = len(p)
rank = np.arange(1,m+1)
harmonic = np.sum(1/rank)


def backward_min(values):
    return np.minimum.accumulate(values[::-1])[::-1]


out = np.column_stack([
    m*p,
    [-expm1(m*log1p(-value)) for value in p],
    np.maximum.accumulate((m-rank+1)*p),
    backward_min((m-rank+1)*p),
    backward_min(m*p/rank),
    backward_min(m*harmonic*p/rank),
]).clip(0,1)
for row, adjusted in zip(rows,out):
    print(row["test"],row["p_raw"],*(round(x,8) for x in adjusted))
counts = (out<=.05).sum(axis=0)
print("rejections:",counts)
assert counts.tolist()==[1,1,2,4,4,1]
