from csv import DictReader
from pathlib import Path

import numpy as np
from scipy.stats import t

with (Path(__file__).resolve().parents[1] / 'data/M47_practice.csv').open() as f:
    rows = list(DictReader(f))
ids = np.array([int(row['id']) for row in rows])
assert len(ids)==len(set(ids))==60
h = np.array([float(row['hours'])-9 for row in rows])
prior = np.array([float(row['prior']) for row in rows])
is_b = np.array([row['group']=='B' for row in rows])
y = np.array([float(row['score']) for row in rows])
intercept = np.ones(len(y))


def fit(design, response):
    coef = np.linalg.lstsq(design,response,rcond=None)[0]
    residual = response-design@coef
    return coef,residual


def vif(predictors,j):
    target = predictors[:,j]
    other = np.delete(predictors,j,axis=1)
    _,residual = fit(np.column_stack([np.ones(len(target)),other]),target)
    centered = target-target.mean()
    return (centered@centered)/(residual@residual)


print("L1:",fit(np.column_stack([intercept,h]),y)[0],
      fit(np.column_stack([intercept,h,prior,is_b]),y)[0])
predictors = np.column_stack([h,is_b,prior,h*is_b])
design = np.column_stack([intercept,predictors])
coef,residual = fit(design,y)
df = len(y)-design.shape[1]
mse = residual@residual/df
inverse = np.linalg.inv(design.T@design)
se = np.sqrt(np.diag(inverse)*mse)
print("L2:",coef[-1],se[-1],2*t.sf(abs(coef[-1]/se[-1]),df),
      [vif(predictors,j) for j in range(predictors.shape[1])])
leverage = np.einsum("ij,jk,ik->i",design,inverse,design)
cook = residual**2/(design.shape[1]*mse)*leverage/(1-leverage)**2
i = cook.argmax()
keep = ids!=60
sensitivity = fit(design[keep],y[keep])[0][-1]
print("L3:",ids[i],residual[i],leverage[i],cook[i],sensitivity)
assert ids[i]==60 and np.isclose(sensitivity,.3629957)
