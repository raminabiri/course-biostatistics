from pathlib import Path

import numpy as np
from scipy.stats import f, ttest_rel

path = Path(__file__).resolve().parents[1] / "data" / "wide.csv"
wide = np.loadtxt(path, delimiter=",", skiprows=1, usecols=(2, 4, 6))
n, k = wide.shape
time_mean = wide.mean(axis=0)
subject_mean = wide.mean(axis=1, keepdims=True)
overall_mean = wide.mean()
residual = wide - subject_mean - time_mean + overall_mean

df_time = k - 1
df_error = (n - 1) * df_time
ss_time = n * np.sum((time_mean - overall_mean) ** 2)
ss_error = np.sum(residual ** 2)
f_value = (ss_time / df_time) / (ss_error / df_error)
print("L1: Time:", f_value, df_time, df_error, f.sf(f_value, df_time, df_error))

u = (wide[:, 0] - wide[:, 1]) / np.sqrt(2)
v = (wide[:, 0] + wide[:, 1] - 2 * wide[:, 2]) / np.sqrt(6)
covariance = np.cov(u, v)
epsilon = np.trace(covariance) ** 2 / (df_time * np.sum(covariance ** 2))
df_time_gg, df_error_gg = epsilon * df_time, epsilon * df_error
print("L2: GG:", epsilon, df_time_gg, df_error_gg, f.sf(f_value, df_time_gg, df_error_gg))

pairs = ((1, 0), (2, 0), (2, 1))
results = [ttest_rel(wide[:, later], wide[:, earlier]) for later, earlier in pairs]
p_raw = np.array([result.pvalue for result in results])
order = np.argsort(p_raw)
adjusted = np.empty_like(p_raw)
adjusted[order] = np.minimum(1, np.maximum.accumulate(p_raw[order] * [3, 2, 1]))
print("L3: paired comparisons")
for i, (later, earlier) in enumerate(pairs):
    change = np.mean(wide[:, later] - wide[:, earlier])
    ci = results[i].confidence_interval()
    print(f"T{later}-T{earlier}: {change:.6f}, CI=({ci.low:.6f}, {ci.high:.6f}),"
          f" P={p_raw[i]:.8g}, Holm={adjusted[i]:.8g}")
