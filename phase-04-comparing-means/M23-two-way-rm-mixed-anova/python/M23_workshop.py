from pathlib import Path
import numpy as np
from scipy.stats import f, ttest_rel, ttest_ind
path=Path(__file__).resolve().parents[1]/"data/practice.csv"
ids,g,tm,b,y=np.loadtxt(path,delimiter=",",skiprows=1,unpack=True)
x=y[b==0].reshape(-1,3)
z=y[b==1].reshape(-1,3)
group=g[(b==0)&(tm==0)]
def rm(y,g=None):
    n,k=y.shape
    g=np.zeros(n) if g is None else g
    centered=y-y.mean(axis=1,keepdims=True)
    lv, idx, w=np.unique(g,return_inverse=True,return_counts=True)
    cells=np.array([centered[g==level].mean(axis=0) for level in lv])
    ss_err=np.sum((centered-cells[idx])**2)
    center=centered.mean(axis=0)
    ss=n*np.sum(center**2) if lv.size==1 else np.sum(w*np.sum((cells-center)**2,axis=1))
    df1=(k-1)*max(1,lv.size-1)
    df2=(n-lv.size)*(k-1)
    value=(ss/df1)/(ss_err/df2)
    return value,f.sf(value,df1,df2)
print("L1:",rm(z-x))
change=x[:,2]-x[:,0]
fit=ttest_ind(change[group==1],change[group==0],equal_var=True)
print("L2:",fit.statistic,fit.pvalue)
print("L3:",rm(x,group))
