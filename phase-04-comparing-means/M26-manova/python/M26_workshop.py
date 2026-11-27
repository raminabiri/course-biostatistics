from pathlib import Path

import numpy as np
from scipy.stats import f

def residual_matrix(design, response):
    coefficients, _, rank, _ = np.linalg.lstsq(design, response, rcond=None)
    residuals = response - design @ coefficients
    return residuals.T @ residuals, rank

def one_df_effect(response, small, large):
    e_small, rank_small = residual_matrix(small, response)
    error, rank_large = residual_matrix(large, response)
    if rank_large - rank_small != 1:
        raise ValueError("This comparison requires one extra model degree of freedom.")
    hypothesis = e_small - error
    root = np.trace(np.linalg.solve(error, hypothesis))
    p = response.shape[1]
    df_error = len(response) - rank_large
    df_f = df_error - p + 1
    statistic = root * df_f / p
    return {
        "Pillai": root / (1 + root), "Wilks": 1 / (1 + root),
        "Hotelling-Lawley": root, "Roy": root, "F": statistic,
        "df1": p, "df2": df_f, "p": f.sf(statistic, p, df_f),
    }

path = Path(__file__).resolve().parents[1] / "data" / "practice.csv"
a, b, y, z, y0, z0 = np.loadtxt(path, delimiter=",", skiprows=1, usecols=(0,1,4,5,6,7), unpack=True)
response = np.column_stack((y,z))
change = response - np.column_stack((y0,z0))
constant = np.ones((len(a),1))
group = np.column_stack((constant,a))
additive = np.column_stack((group,b))
interaction = np.column_stack((additive,a*b))

print("L1: end by group", one_df_effect(response, constant, group))
print("L2: end interaction", one_df_effect(response, additive, interaction))
print("L3: change by group", one_df_effect(change, constant, group))
