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
a,b,c,k,y=np.loadtxt(path,delimiter=",",skiprows=1,unpack=True)
o=np.ones(y.size)
s=c==0
print("L1:",nested_test(y[s],np.column_stack([o,a,b])[s],np.column_stack([o,a,b,a*b])[s]))
print("L2:", y[s&(b==1)&(a==1)].mean()-y[s&(b==1)&(a==0)].mean())
base=np.column_stack([o,a,b,c,a*b,a*c,b*c])
print("L3:",nested_test(y,base,np.column_stack([base,a*b*c])))
