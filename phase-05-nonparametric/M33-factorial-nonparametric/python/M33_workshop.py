from pathlib import Path

from scipy.stats import chi2, f, rankdata
import numpy as np

def nested_test(y, reduced, full):
    def residual_ss(x):
        coefficient, _, rank, _ = np.linalg.lstsq(x, y, rcond=None)
        residual = y - x @ coefficient
        return residual @ residual, rank
    ss0, rank0 = residual_ss(reduced)
    ss1, rank1 = residual_ss(full)
    df1, df2 = rank1-rank0, len(y)-rank1
    statistic = ((ss0-ss1)/df1)/(ss1/df2)
    return statistic, f.sf(statistic, df1, df2)
path=Path(__file__).resolve().parents[1]/"data/practice.csv"
a,b,i,x,y=np.loadtxt(path,delimiter=",",skiprows=1,unpack=True)
counts = np.array([np.sum((a == i) & (b == j)) for i in (0, 1) for j in (0, 1)])
if not (np.all(counts == counts[0]) and counts[0] >= 2 and counts.sum() == y.size):
    raise ValueError("This workshop requires a complete balanced 2×2 design")
o=np.ones(y.size)
orthogonal=np.column_stack([o,a-.5,b-.5,(a-.5)*(b-.5)])
ma=np.array([y[a==g].mean() for g in a])
mb=np.array([y[b==g].mean() for g in b])
cell=np.array([y[(a==aa)&(b==bb)].mean() for aa,bb in zip(a,b)])
grand=y.mean()
aligned=[y-cell+ma-grand,y-cell+mb-grand,y-ma-mb+grand]
for j,col in enumerate(aligned,1):
    unwanted = np.delete(orthogonal, j, axis=1)
    assert np.allclose(unwanted.T @ col, 0, atol=1e-10), "Check alignment"
    print("L1",j,nested_test(rankdata(np.round(col,10)),np.delete(orthogonal,j,axis=1),orthogonal))
r=rankdata(y)
coef=np.linalg.lstsq(orthogonal,r,rcond=None)[0]
ss=np.sum((orthogonal[:,1:]*coef[1:])**2,axis=0)
h=ss/r.var(ddof=1)
print("L2:",h,chi2.sf(h,1))
mask=b==0
rx=rankdata(x[mask])
ry=rankdata(y[mask])
xbase=np.column_stack([o[mask],rx])
adj=ry-xbase@np.linalg.lstsq(xbase,ry,rcond=None)[0]
print("L3:",nested_test(adj,o[mask,None],np.column_stack([o[mask],a[mask]])))
