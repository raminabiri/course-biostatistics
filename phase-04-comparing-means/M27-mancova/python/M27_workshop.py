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
a, b, baseline, y, z = np.loadtxt(path, delimiter=",", skiprows=1, usecols=(0,1,3,4,5), unpack=True)
x = baseline - 25
response = np.column_stack((y,z))
ones = np.ones(len(a))
b0 = b == 0

simple = np.column_stack((ones,x))[b0]
adjusted = np.column_stack((simple,a[b0]))
coef = np.linalg.lstsq(adjusted,response[b0],rcond=None)[0]
print("L1 adjusted predictions at 25:", np.array([[1,0,0],[1,0,1]]) @ coef)
print("L1 effect A in B0:", one_df_effect(response[b0],simple,adjusted))

additive = np.column_stack((ones,a,b,x))
factorial = np.column_stack((additive,a*b))
slopes = np.column_stack((factorial,a*x))
print("L2 effect A:B:", one_df_effect(response,additive,factorial))
print("L3 effect A:x:", one_df_effect(response,factorial,slopes))
print("Coefficients of A:x:", np.linalg.lstsq(slopes,response,rcond=None)[0][-1])
