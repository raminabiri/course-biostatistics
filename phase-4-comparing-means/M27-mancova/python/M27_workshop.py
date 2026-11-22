from pathlib import Path
import numpy as np
from scipy import stats

path = Path(__file__).resolve().parents[1] / "data/practice.csv"
a, b, i, x, y1, y2, y01, y02 = np.loadtxt(path, delimiter=",", skiprows=1, unpack=True)
y = np.column_stack([y1, y2])
def multivariate(response, reduced, full):
    reduced,full=np.column_stack(reduced),np.column_stack(full)
    def residual_cross(design):
        coef,_,rank,_=np.linalg.lstsq(design,response,rcond=None)
        residual=response-design@coef
        return residual.T@residual,rank
    e0,r0=residual_cross(reduced)
    e,r1=residual_cross(full)
    roots=np.maximum(np.linalg.eigvals(np.linalg.solve(e,e0-e)).real,0)
    p=response.shape[1]
    assert r1-r0==1
    df2=len(response)-r1-p+1
    stat=roots.sum()*df2/p
    return np.sum(roots/(1+roots)),np.prod(1/(1+roots)),roots.sum(),roots.max(),stat,stats.f.sf(stat,p,df2)

o=np.ones(len(a))
s=b==0
design=np.column_stack([o,a,x])
coef=np.linalg.lstsq(design[s],y[s],rcond=None)[0]
print("Predicted at baseline 25:",np.array([[1,0,25],[1,1,25]])@coef)
print("L1:",multivariate(y[b==0],[o[b==0],x[b==0]],[o[b==0],x[b==0],a[b==0]]))
print("L2:",multivariate(y,[o,a,b,x],[o,a,b,x,a*b]))
print("L3:",multivariate(y,[o,a,b,x,a*b],[o,a,b,x,a*b,a*x]))
