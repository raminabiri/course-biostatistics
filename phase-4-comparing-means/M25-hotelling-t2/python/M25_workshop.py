from pathlib import Path
import numpy as np
from scipy import stats

path = Path(__file__).resolve().parents[1] / "data/practice.csv"
a, b, i, x, y1, y2, y01, y02 = np.loadtxt(path, delimiter=",", skiprows=1, unpack=True)
y = np.column_stack([y1, y2])
def test(d, cov, weight, denom, df2):
    tt = weight * d @ np.linalg.solve(cov, d)
    ff = tt * df2 / (len(d)*denom)
    return tt, ff, stats.f.sf(ff,len(d),df2)
def one(z, mu):
    n,p=z.shape
    return test(z.mean(axis=0)-mu,np.cov(z,rowvar=False),n,n-1,n-p)
u,v=y[a==0],y[a==1]
print("L1:",one(u,np.array([47,27])))
print("L2:",test(v.mean(axis=0)-u.mean(axis=0),(np.cov(u,rowvar=False)+np.cov(v,rowvar=False))/2,8,30,29))
print("L3:",one(y-np.column_stack([y01,y02]),np.zeros(2)))
