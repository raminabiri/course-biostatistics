from pathlib import Path

import numpy as np

directory = Path(__file__).resolve().parents[1] / "data"
two = np.loadtxt(directory / "M42_two.csv", delimiter=",", skiprows=1, dtype=int)
table = np.zeros((3, 3), dtype=int)
np.add.at(table, (two[:,1],two[:,2]), 1)
o = table/table.sum()
e = np.outer(o.sum(axis=1),o.sum(axis=0))
gap = np.abs(np.subtract.outer(np.arange(3),np.arange(3)))/2
for name,w in (("simple",np.eye(3)),("linear",1-gap),("quadratic",1-gap**2)):
    a, b = (o*w).sum(), (e*w).sum()
    print(name,a,b,(a-b)/(1-b))
scores = np.loadtxt(directory / "M42_multiple.csv", delimiter=",", skiprows=1, dtype=int)[:,1:]
v = np.column_stack([(scores==category).sum(axis=1) for category in range(3)])
assert np.all(v.sum(axis=1)==3)
p = v.sum(axis=0)/v.sum()
a = (np.sum(v*(v-1),axis=1)/6).mean()
f, g = p@p, np.sum(p*(1-p))/2
print("L3:",v.sum(axis=0),a,(a-f)/(1-f),(a-g)/(1-g))
assert np.isclose((a-g)/(1-g),.649567619)
