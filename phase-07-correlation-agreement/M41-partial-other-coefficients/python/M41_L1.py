from pathlib import Path

import numpy as np
from scipy import stats

p = Path(__file__).resolve().parents[1] / "data/M41_practice.csv"
_, age, x, y = np.loadtxt(p, delimiter=",", skiprows=1, unpack=True)
design = np.column_stack([np.ones(len(age)), age])


def residual(values, predictors):
    coef = np.linalg.lstsq(predictors, values, rcond=None)[0]
    return values - predictors @ coef


rx, ry = residual(x, design), residual(y, design)
r = stats.pearsonr(rx, ry).statistic
semi = stats.pearsonr(rx, y).statistic
df = len(y)-3
t = r*np.sqrt(df/(1-r*r))
full_residual = residual(y,np.column_stack([design,x]))
centered = y-y.mean()
delta = (ry@ry-full_residual@full_residual)/(centered@centered)
print(stats.pearsonr(x,y).statistic,r,semi,delta,2*stats.t.sf(abs(t),df))
assert np.isclose(semi*semi,delta)
