ra,rb=15/100,25/100
difference=105-100
v=(difference,difference/10,ra,rb,rb-ra,ra/rb,1/(rb-ra),(5/2.5)**2)
from math import isclose
assert all(isclose(a,b,abs_tol=1e-6) for a,b in zip(v,[5, 0.5, 0.15, 0.25, 0.1, 0.6, 10, 4],strict=True))
print(v)
