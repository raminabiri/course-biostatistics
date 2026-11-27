from csv import DictReader
from pathlib import Path

import numpy as np
from scipy.stats import t

with (Path(__file__).resolve().parents[1] / "data/M46_practice.csv").open() as f:
    rows = list(DictReader(f))
assert len(rows)==len({row["id"] for row in rows})==24
minutes = np.array([float(row["minutes"]) for row in rows])
score = np.array([float(row["score"]) for row in rows])
is_b = np.array([row["group"]=="B" for row in rows])


def fit(design,y):
    coef = np.linalg.lstsq(design,y,rcond=None)[0]
    residual = y-design@coef
    df = len(y)-design.shape[1]
    error_variance = (residual@residual)/df
    covariance = error_variance*np.linalg.inv(design.T@design)
    se = np.sqrt(covariance.diagonal())
    return coef,residual,df,error_variance,covariance,se


x, y = minutes[~is_b], score[~is_b]
coef,residual,df,error_variance,covariance,se = fit(np.column_stack([np.ones(len(x)),x]),y)
centered = y-y.mean()
print("L1:",coef,residual[0],1-(residual@residual)/(centered@centered),
      2*t.sf(abs(coef[1]/se[1]),df))
vector = np.array([1,15])
point = vector@coef
mean_variance = vector@covariance@vector
for kind,variance in [("mean",mean_variance),("new",mean_variance+error_variance)]:
    width=t.ppf(.975,df)*np.sqrt(variance)
    print("L2:",kind,point,point-width,point+width)
design = np.column_stack([np.ones(len(minutes)),minutes,is_b,minutes*is_b])
coef,_,df,_,_,se = fit(design,score)
print("L3:",coef[-1],se[-1],2*t.sf(abs(coef[-1]/se[-1]),df))
assert np.isclose(coef[-1],.473776224)
