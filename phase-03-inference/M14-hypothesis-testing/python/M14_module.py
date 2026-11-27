from math import sqrt
from scipy.stats import t
se=10/sqrt(25)
stat=(104-100)/se
df=24
p=2*t.sf(abs(stat),df)
half=t.ppf(.975,df)*se
v=(se,stat,df,p,104-half,104+half)
from math import isclose
assert all(isclose(a,b,abs_tol=1e-6) for a,b in zip(v,[2, 2, 24, 0.0569398499, 99.8722028767, 108.1277971233],strict=True))
print(v)
