from pathlib import Path

import numpy as np
from scipy.optimize import linprog,minimize

file = Path(__file__).resolve().parents[1] / 'data/M48_practice.csv'
_,x,y = np.loadtxt(file,delimiter=',',skiprows=1,unpack=True)
n=len(x)
design = np.column_stack([np.ones(n),x])
h = (np.maximum(x-4,0)**3-2*np.maximum(x-12,0)**3+np.maximum(x-20,0)**3)/256


def ols(matrix):
    coefficients = np.linalg.lstsq(matrix,y,rcond=None)[0]
    residual = y-matrix@coefficients
    return coefficients,residual@residual


print("L1:",[ols(v)[1] for v in (design,np.column_stack([design,x*x]),np.column_stack([design,h]))])


def huber(coef):
    u = np.abs((y-design@coef)/2)
    return np.where(u<=1.345,u*u/2,1.345*(u-1.345/2)).sum()


ordinary = ols(design)[0]
robust = minimize(huber,ordinary,method='BFGS')
assert robust.success
print("L2:",ordinary,robust.x)
for tau in (.5,.9):
    costs=np.r_[0,0,np.full(n,tau),np.full(n,1-tau)]
    equation=np.column_stack([design,np.eye(n),-np.eye(n)])
    result=linprog(costs,A_eq=equation,b_eq=y,bounds=[(None,None)]*2+[(0,None)]*(2*n))
    assert result.success
    print("L3:",tau,result.x[:2],result.fun)
