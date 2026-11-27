from scipy.stats import f
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
from pathlib import Path
path=Path(__file__).resolve().parents[1]/"data/practice.csv"
a,b,i,x,y=np.loadtxt(path,delimiter=",",skiprows=1,unpack=True)
x=x-24
o=np.ones(y.size)
s=b==0
coef=np.linalg.lstsq(np.column_stack([o,a,x])[s], y[s],rcond=None)[0]
print("L1:",coef[0],coef[0]+coef[1])
base=np.column_stack([o,a,b,x])
print("L2:",nested_test(y,base,np.column_stack([base,a*b])))
change=2+1.5*a[s]+.3*x[s]+np.array([-1,1,0,2,-2,1,0,1,-1,0,2,-1])
print("L3:",nested_test(change,np.column_stack([o,x])[s],np.column_stack([o,x,a])[s]))
