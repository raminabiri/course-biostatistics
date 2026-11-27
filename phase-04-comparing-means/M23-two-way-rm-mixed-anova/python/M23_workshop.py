import csv
from pathlib import Path

import numpy as np
from scipy.stats import f, ttest_ind

path = Path(__file__).resolve().parents[1] / "data" / "wide.csv"
with path.open(newline="", encoding="utf-8") as stream:
    rows = list(csv.DictReader(stream))

def matrix(condition):
    columns = [f"t{time}c{condition}" for time in range(3)]
    return np.array([[float(row[name]) for name in columns] for row in rows])

if len({row["id"] for row in rows}) != len(rows):
    raise ValueError("Each participant must have exactly one row.")

zero = matrix(0)
one = matrix(1)
if not np.isfinite(zero).all() or not np.isfinite(one).all():
    raise ValueError("The ANOVA workbook requires complete measurements.")
group = np.array([int(row["group"]) for row in rows])

def time_test(values, groups):
    n, k = values.shape
    centered = values - values.mean(axis=1, keepdims=True)
    levels, indices, counts = np.unique(groups, return_inverse=True, return_counts=True)
    profiles = np.array([centered[groups == level].mean(axis=0) for level in levels])
    ss_error = np.sum((centered - profiles[indices]) ** 2)
    overall = centered.mean(axis=0)
    if levels.size == 1:
        ss_effect = n * np.sum(overall ** 2)
    else:
        ss_effect = np.sum(counts * np.sum((profiles - overall) ** 2, axis=1))
    df_effect = (k - 1) * max(1, levels.size - 1)
    df_error = (n - levels.size) * (k - 1)
    statistic = (ss_effect / df_effect) / (ss_error / df_error)
    return statistic, df_effect, df_error, f.sf(statistic, df_effect, df_error)

print("L1: F, degrees of freedom, P:", time_test(one - zero, np.zeros(len(rows))))
change = zero[:, 2] - zero[:, 0]
first, second = change[group == 1], change[group == 0]
fit = ttest_ind(first, second, equal_var=True)
print("L2: Difference, t, degrees of freedom, P:", first.mean() - second.mean(), fit.statistic, fit.df, fit.pvalue)
print("L2: 95% CI:", fit.confidence_interval())
print("L3: F, degrees of freedom, P:", time_test(zero, group))
