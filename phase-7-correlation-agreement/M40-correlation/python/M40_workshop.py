from csv import DictReader
from math import atanh, isclose, sqrt
from pathlib import Path

import numpy as np
from scipy import stats

with (Path(__file__).resolve().parents[1] / "data/M40_practice.csv").open() as f:
    rows = list(DictReader(f))
assert len(rows) == len({row["id"] for row in rows}) == 60


def values(group):
    return np.array([[float(row[key]) for key in ("age", "marker_x", "marker_y")]
                     for row in rows if row["group"] == group])


a, b = values("A"), values("B")
assert len(a) == len(b) == 30
x, y = a[:,1], a[:,2]
result = stats.pearsonr(x,y)
right = stats.pearsonr(x,y,alternative="greater").pvalue
print("L1:",result.statistic,result.pvalue,right)
print("L2:",stats.spearmanr(x,y).statistic,stats.kendalltau(x,y,variant="b").statistic)
print(np.corrcoef(a,rowvar=False))
r1, r2 = result.statistic, stats.pearsonr(b[:,1],b[:,2]).statistic
z = (atanh(r1)-atanh(r2))/sqrt(1/(len(a)-3)+1/(len(b)-3))
print("L3:",r1,r2,z,2*stats.norm.sf(abs(z)))
assert isclose(r1,.7855360872) and isclose(z,2.9092349744)
