from itertools import product
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, minimize
from scipy.special import expit, logsumexp

source = Path(__file__).resolve().parents[1] / "data"
scale = np.loadtxt(source/"M44_scale.csv",delimiter=",",skiprows=1)[:,1:]
raw = scale[:,:5].copy()
scores = raw.copy()
scores[:,3] = 6-scores[:,3]


def alpha(x):
    k = x.shape[1]
    return k/(k-1)*(1-x.var(axis=0,ddof=1).sum()/x.sum(axis=1).var(ddof=1))


total = scores.sum(axis=1)
item_total = [np.corrcoef(scores[:,j],total-scores[:,j])[0,1] for j in range(5)]
print("L1:",alpha(raw),alpha(scores),item_total)
r = np.corrcoef(scores,rowvar=False)


def factor_objective(loadings):
    sigma = np.outer(loadings,loadings)+np.diag(1-loadings**2)
    return np.linalg.slogdet(sigma)[1]+np.trace(np.linalg.solve(sigma,r))


factor = minimize(factor_objective,[.7]*5,bounds=[(-.997,.997)]*5)
assert factor.success
l = factor.x
omega = l.sum()**2/(l.sum()**2+(1-l*l).sum())
print("L2:",l,omega,np.corrcoef(total,scale[:,5])[0,1])
x = np.loadtxt(source/"M44_rasch.csv",delimiter=",",skiprows=1,dtype=int)[:,1:]
k = x.shape[1]
patterns = np.array(list(product((0,1),repeat=k)))
pattern_scores = patterns.sum(axis=1)
row_scores = x.sum(axis=1)
counts = np.bincount(row_scores,minlength=k+1)
total_by_item = x.sum(axis=0)


def difficulties(free):
    return np.r_[free,-free.sum()]


def negative_conditional_likelihood(free):
    delta = difficulties(free)
    normalization = sum(counts[s]*logsumexp(-patterns[pattern_scores==s]@delta)
                        for s in range(k+1))
    return total_by_item@delta+normalization


rasch = minimize(negative_conditional_likelihood,np.zeros(k-1),method="BFGS",
                 options={"gtol":1e-5})
d = difficulties(rasch.x)
theta3 = brentq(lambda ability: expit(ability-d).sum()-3,-15,15)
print("L3:",total_by_item,counts,d,theta3,expit(theta3-d))
assert np.isclose(omega,.83618,atol=.0001) and abs(d.sum())<1e-12
