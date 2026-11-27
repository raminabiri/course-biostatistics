from pathlib import Path

import numpy as np
from scipy.stats import f, t

data_dir = Path(__file__).resolve().parents[1] / "data"

def fit(design, response):
    coefficients, _, rank, _ = np.linalg.lstsq(design, response, rcond=None)
    residual = response - design @ coefficients
    return coefficients, residual @ residual, len(response) - rank

def nested_test(outcome, smaller, larger):
    _, ss_small, df_small = fit(smaller, outcome)
    _, ss_large, df_large = fit(larger, outcome)
    df_effect = df_small - df_large
    statistic = (max(0, ss_small - ss_large) / df_effect) / (ss_large / df_large)
    return statistic, f.sf(statistic, df_effect, df_large)

def group_interval(design, response, index):
    coefficients, ss, df = fit(design, response)
    variance = (ss / df) * np.linalg.inv(design.T @ design)[index, index]
    margin = t.ppf(.975, df) * np.sqrt(variance)
    return coefficients[index] - margin, coefficients[index] + margin

a, b, _, baseline, value = np.loadtxt(data_dir / "practice.csv", delimiter=",", skiprows=1, unpack=True)
x = baseline - 24
ones = np.ones(len(value))
is_b0 = b == 0
design_b0 = np.column_stack((ones, a, x))[is_b0]
fit_b0, _, _ = fit(design_b0, value[is_b0])
print("L1: adjusted means", fit_b0[0], fit_b0[0] + fit_b0[1])
print("L1: difference CI", group_interval(design_b0, value[is_b0], 1))
print("L1: slope test", nested_test(value[is_b0], design_b0, np.column_stack((design_b0, (a*x)[is_b0]))))

base = np.column_stack((ones, a, b, x))
common = np.column_stack((base, a*b))
varying = np.column_stack((common, a*x, b*x, a*b*x))
print("L2: A by B", nested_test(value, base, common))
print("L2: slopes", nested_test(value, common, varying))

a, baseline, change = np.loadtxt(data_dir / "change.csv", delimiter=",", skiprows=1, unpack=True)
base = np.column_stack((np.ones(len(change)), baseline - 24))
model = np.column_stack((base, a))
coef, _, _ = fit(model, change)
print("L3: change", nested_test(change, base, model))
print("L3: difference and CI", coef[2], group_interval(model, change, 2))
