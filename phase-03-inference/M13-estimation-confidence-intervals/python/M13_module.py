from math import sqrt
from scipy.stats import t,norm
se=10/sqrt(25)
width=t.ppf(.975,24)*se
p=18/30
z=norm.ppf(.975)
center=(p+z*z/60)/(1+z*z/30)
half=z*sqrt(p*(1-p)/30+z*z/3600)/(1+z*z/30)
v=(se,100-width,100+width,p,center-half,center+half,105-100,sqrt(8))
from math import isclose
assert all(isclose(a,b,abs_tol=1e-6) for a,b in zip(v,[2, 95.8722028767, 104.1277971233, 0.6, 0.4232036025, 0.7540937188, 5, 2.8284271247],strict=True))
print(v)
