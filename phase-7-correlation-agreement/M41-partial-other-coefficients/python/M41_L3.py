from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import minimize_scalar

p = Path(__file__).resolve().parents[1] / "data/M41_practice.csv"
_, _, x, y = np.loadtxt(p, delimiter=",", skiprows=1, unpack=True)
binary = np.zeros((2,2),dtype=int)
ordinal = np.zeros((3,3),dtype=int)
np.add.at(binary,((x>=55).astype(int),(y>=65).astype(int)),1)
np.add.at(ordinal,(np.digitize(x,[45,65]),np.digitize(y,[55,75])),1)


def edges(margin):
    return np.r_[-np.inf,stats.norm.ppf(np.cumsum(margin)[:-1]/margin.sum()),np.inf]


def estimate(table):
    a, b = edges(table.sum(axis=1)), edges(table.sum(axis=0))

    def loss(rho):
        result = 0
        for i, j in zip(*np.nonzero(table)):
            probability = stats.multivariate_normal.cdf(
                [a[i+1],b[j+1]], cov=[[1,rho],[rho,1]], lower_limit=[a[i],b[j]]
            )
            result -= table[i,j]*np.log(probability)
        return result

    return minimize_scalar(loss,bounds=(-.98,.98),method="bounded").x


out = estimate(binary),estimate(ordinal)
print("tetrachoric, polychoric:",out)
assert np.allclose(out,[.827761,.892447],atol=1e-5)
