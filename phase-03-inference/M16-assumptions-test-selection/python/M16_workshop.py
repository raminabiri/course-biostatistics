from pathlib import Path
from math import sqrt
import numpy as np
from scipy import stats

file = Path(__file__).resolve().parents[1] / "data/M16_groups.csv"
a, b = np.loadtxt(file, delimiter=",", skiprows=1, unpack=True)
sw = stats.shapiro(a)
bf = stats.levene(a, b, center="median")
bt = stats.bartlett(a, b)
n = a.size
q = stats.t.ppf(1-.05/(2*n), n-2)
cut = (n-1)/sqrt(n)*sqrt(q*q/(n-2+q*q))
grubbs = max(abs(a-a.mean()))/a.std(ddof=1)
welch = stats.ttest_ind(a,b,equal_var=False)
assert abs(sw.pvalue-.01404)<.0001 and abs(bf.pvalue-.26917)<.0001
assert grubbs > cut and abs(welch.pvalue-.21865)<.0001
print("L1:", sw)
print("L2:", bf, bt)
print("L3:", grubbs, cut)
print("L4:", welch)
