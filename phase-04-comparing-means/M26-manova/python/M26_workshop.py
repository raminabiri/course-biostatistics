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
print("L1:",multivariate(y,[o],[o,a]))
print("L2:",multivariate(y,[o,a,b],[o,a,b,a*b]))
print("L3:",multivariate(y-np.column_stack([y01,y02]),[o],[o,a]))
