from scipy.stats import f, t
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
import csv
from pathlib import Path
path=Path(__file__).resolve().parents[1]/"data/practice.csv"
with path.open() as file:
    data=list(csv.DictReader(file))
def rows(name):
    chosen=[[float(r[c]) for c in ("u","v","w","period","value")] for r in data if r["design"]==name]
    return np.array(chosen).T
def codes(x):
    return np.column_stack([x==value for value in np.unique(x)[1:]])
u,v,w,period,y=rows("block")
base=np.column_stack([np.ones(y.size),codes(u)])
print("L1 block:",nested_test(y,base,np.column_stack([base,codes(w)])))
u,v,w,period,y=rows("latin")
base=np.column_stack([np.ones(y.size),codes(u),codes(v)])
print("L1 Latin:",nested_test(y,base,np.column_stack([base,codes(w)])))
u,v,w,period,y=rows("nested")
grand=y.mean()
ss_a=sum(np.sum(u==a)*(y[u==a].mean()-grand)**2 for a in np.unique(u))
ss_lab=sum(np.sum((u==a)&(v==b))*(y[(u==a)&(v==b)].mean()-y[u==a].mean())**2 for a in np.unique(u) for b in np.unique(v))
ss_err=sum(np.sum((y[(u==a)&(v==b)]-y[(u==a)&(v==b)].mean())**2) for a in np.unique(u) for b in np.unique(v))
ff=ss_a/(ss_lab/4)
print("L2:",ff,f.sf(ff,1,4),(ss_lab/4-ss_err/18)/4)
u,v,w,period,y=rows("cross")
base=np.column_stack([np.ones(y.size),codes(u),period])
full=np.column_stack([base,w])
coef=np.linalg.lstsq(full,y,rcond=None)[0]
print("L3:",coef[-1],nested_test(y,base,full)[1])

full_error = y - full @ coef
df = len(y) - np.linalg.matrix_rank(full)
variance = (full_error @ full_error) / df
standard_error = np.sqrt(variance * np.linalg.inv(full.T @ full)[-1, -1])
margin = t.ppf(.975, df) * standard_error
print("L3: period effect", coef[-2])
print("L3: treatment 95% CI", coef[-1] - margin, coef[-1] + margin)
