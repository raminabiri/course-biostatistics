from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats

source = Path(__file__).resolve().parents[1] / "data/M36_practice.csv"
ids, dose, response, total = np.loadtxt(source, delimiter=",", skiprows=1, unpack=True, dtype=int)
assert ids.size == np.unique(ids).size == 120
score = dose - dose.mean()
p = total.mean()
z = (score @ total) / np.sqrt(p*(1-p)*(score**2).sum())
r = stats.pearsonr(dose, response).statistic
x2 = (len(dose)-1)*r*r
table = np.zeros((3, 3), dtype=int)
np.add.at(table, (dose, response), 1)
concordant = discordant = 0
for i, ii in combinations(range(3), 2):
    for j, jj in combinations(range(3), 2):
        concordant += table[i, j] * table[ii, jj]
        discordant += table[i, jj] * table[ii, j]
gamma = (concordant-discordant)/(concordant+discordant)
print("L1:", z, stats.norm.sf(z), 2*stats.norm.sf(abs(z)))
print("L2:", r, x2, stats.chi2.sf(x2, 1))
print("L3:", concordant, discordant, gamma)
assert (concordant, discordant) == (2356, 876)
assert np.isclose(z, 3.1749015733)
