from math import atanh, ceil, sqrt
from statistics import NormalDist

n = NormalDist()
a,b = n.inv_cdf(.975),n.inv_cdf(.8)
p = (a*sqrt(2*.25*.75)+b*sqrt(.2*.8+.3*.7))**2/(.3-.2)**2
c = 3+((a+b)/atanh(.3))**2
print(p,c,ceil(p),ceil(c))
assert (ceil(p),ceil(c))==(294,85)
