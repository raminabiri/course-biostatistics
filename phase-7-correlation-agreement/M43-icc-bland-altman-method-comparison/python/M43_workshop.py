from itertools import combinations
from pathlib import Path

import numpy as np

source = Path(__file__).resolve().parents[1] / "data/M43_methods.csv"
_, a, b = np.loadtxt(source, delimiter=",", skiprows=1, unpack=True)
x = np.column_stack((a,b))
n,k = x.shape
overall = x.mean()
case_mean = x.mean(axis=1)
method_mean = x.mean(axis=0)
msi = k*np.sum((case_mean-overall)**2)/(n-1)
msr = n*np.sum((method_mean-overall)**2)/(k-1)
within = x-case_mean[:,None]
mse = np.sum((within-method_mean+overall)**2)/((n-1)*(k-1))
msw = np.sum(within**2)/(n*(k-1))
icc = ((msi-msw)/(msi+(k-1)*msw),
       (msi-mse)/(msi+(k-1)*mse+k*(msr-mse)/n),
       (msi-mse)/(msi+(k-1)*mse),
       (msi-mse)/(msi+(msr-mse)/n))
print("L1:",msi,msr,mse,msw,icc)
difference = b-a
mean, sd = difference.mean(),difference.std(ddof=1)
cov = np.cov(a,b,ddof=0)
ccc = 2*cov[0,1]/(np.trace(cov)+(a.mean()-b.mean())**2)
print("L2:",mean,sd,mean-1.96*sd,mean+1.96*sd,ccc)
delta = cov[1,1]-cov[0,0]
sxy = cov[0,1]
deming = (delta+np.sqrt(delta**2+4*sxy**2))/(2*sxy)
slopes = np.array([(b[j]-b[i])/(a[j]-a[i]) for i,j in combinations(range(n),2)])
assert np.all(np.isfinite(slopes) & (slopes > -1))
pb = np.median(slopes)
print("L3:",deming,b.mean()-deming*a.mean(),pb,np.median(b-pb*a))
assert n==24 and np.isclose(icc[1],.9585648192) and np.isclose(pb,1.06)
