from pathlib import Path

import numpy as np
from scipy import stats

path = Path(__file__).resolve().parents[1] / "data" / "practice.csv"
group, y, z, y0, z0 = np.loadtxt(path, delimiter=",", skiprows=1, unpack=True,
                                usecols=(0, 4, 5, 6, 7))
after = np.column_stack((y, z))
before = np.column_stack((y0, z0))

def test(delta, covariance, weight, df_covariance, df_f):
    p = len(delta)
    t_squared = weight * (delta @ np.linalg.solve(covariance, delta))
    f_value = t_squared * df_f / (p * df_covariance)
    return t_squared, f_value, stats.f.sf(f_value, p, df_f)

def one_sample(values, reference):
    n, p = values.shape
    return test(values.mean(axis=0)-reference, np.cov(values, rowvar=False), n, n-1, n-p)

left, right = after[group == 0], after[group == 1]
n0, n1 = len(left), len(right)
n = n0 + n1
s0, s1 = np.cov(left, rowvar=False), np.cov(right, rowvar=False)
pooled = ((n0 - 1) * s0 + (n1 - 1) * s1) / (n - 2)

print("L1:", one_sample(left, np.array([47, 27])))
print("L2:", test(right.mean(axis=0)-left.mean(axis=0), pooled, n0*n1/n, n-2, n-3))
change = after - before
print("L3:", one_sample(change, np.zeros(2)))
p = change.shape[1]
factor = p*(n-1)/(n-p)*stats.f.ppf(.95, p, n-p)
margin = np.sqrt(factor*np.diag(np.cov(change, rowvar=False))/n)
print("L3 simultaneous intervals:", np.column_stack((change.mean(axis=0)-margin, change.mean(axis=0)+margin)))
