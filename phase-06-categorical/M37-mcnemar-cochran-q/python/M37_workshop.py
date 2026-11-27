from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats

root = Path(__file__).resolve().parents[1] / 'data'
ids, before, after = np.loadtxt(
    root / 'M37_transition.csv', delimiter=',', skiprows=1, unpack=True, dtype=int
)
assert ids.size == np.unique(ids).size == 80
up = np.sum((before != 2) & (after == 2))
down = np.sum((before == 2) & (after != 2))
table = np.zeros((3, 3), dtype=int)
np.add.at(table, (before, after), 1)
bowker = sum((table[i,j]-table[j,i])**2/(table[i,j]+table[j,i])
             for i,j in combinations(range(3),2))
row_counts = table.sum(axis=1)
column_counts = table.sum(axis=0)
v = -(table+table.T)
np.fill_diagonal(v, row_counts+column_counts-2*table.diagonal())
delta = (row_counts-column_counts)[:2]
sm = delta @ np.linalg.solve(v[:2,:2],delta)
x = np.loadtxt(root / 'M37_repeated.csv', delimiter=',', skiprows=1, dtype=int)[:,1:]
k = x.shape[1]
total = x.sum()
column_totals = x.sum(axis=0)
q = (k-1)*(k*np.sum(column_totals**2)-total**2)/(k*total-np.sum(x.sum(axis=1)**2))
print('L1:',up,down,stats.binomtest(up,up+down,.5).pvalue)
print('L2:',bowker,stats.chi2.sf(bowker,3),sm,stats.chi2.sf(sm,2))
print('L3:',column_totals,q,stats.chi2.sf(q,2))
assert x.shape == (50,3) and np.isclose(q,14/3)
