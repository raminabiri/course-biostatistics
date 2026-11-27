import numpy as np
from scipy import stats
groups = [np.array(x, dtype=float) for x in ([48,50,51,52,53],[51,52,55,56,57],[54,58,59,62,65])]
print("L1:",stats.f_oneway(*groups))
n = np.array([len(x) for x in groups])
means = np.array([x.mean() for x in groups])
variances = np.array([x.var(ddof=1) for x in groups])
w = n/variances
k = len(n)
u = np.sum((1-w/w.sum())**2/(n-1))
fw = np.sum(w*(means-np.average(means,weights=w))**2)/(k-1)/(1+2*(k-2)*u/(k*k-1))
v = (1-n/n.sum())*variances
bf = np.sum(n*(means-np.average(means,weights=n))**2)/v.sum()
df = v.sum()**2/np.sum(v*v/(n-1))
print("L2 Welch:",fw,stats.f.sf(fw,k-1,(k*k-1)/(3*u)))
print("L2 Brown-Forsythe:",bf,stats.f.sf(bf,k-1,df))
print("L3 contrast:",means[-1]-means[0])
print(stats.tukey_hsd(*groups))
