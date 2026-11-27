from statistics import mean,stdev
from math import sqrt
d=(2,-1,3)
x=(2,3,4,5,20)
v=(mean(d),stdev(d)/sqrt(len(d)),6**2/2**2,mean(x),mean(x[:-1]))
from math import isclose
assert all(isclose(a,b,abs_tol=1e-6) for a,b in zip(v,[1.3333333333333333, 1.2018504251546631, 9, 6.8, 3.5],strict=True))
print(v)
