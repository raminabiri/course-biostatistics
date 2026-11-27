from pathlib import Path

import numpy as np
from scipy import stats

p = Path(__file__).resolve().parents[1] / "data/M41_practice.csv"
_, _, x, y = np.loadtxt(p, delimiter=",", skiprows=1, unpack=True)
high_x, high_y = x>=55,y>=65
gx, gy = np.digitize(x,[45,65]), np.digitize(y,[55,75])
two = np.zeros((2,2),dtype=int)
three = np.zeros((3,3),dtype=int)
np.add.at(two,(high_x.astype(int),high_y.astype(int)),1)
np.add.at(three,(gx,gy),1)
p_high = high_x.mean()
pb = stats.pointbiserialr(high_x,y).statistic
biserial = pb*np.sqrt(p_high*(1-p_high))/stats.norm.pdf(stats.norm.ppf(1-p_high))
x2 = stats.chi2_contingency(three,correction=False).statistic
centered = y-y.mean()
between = sum(np.sum(gx==i)*(y[gx==i].mean()-y.mean())**2 for i in range(3))
eta = np.sqrt(between/(centered@centered))
print(two,three)
print(pb,biserial,stats.pearsonr(high_x,high_y).statistic,
      np.sqrt(x2/(2*len(y))),np.sqrt(x2/(x2+len(y))),eta)
assert np.isclose(eta,.7676913121)
