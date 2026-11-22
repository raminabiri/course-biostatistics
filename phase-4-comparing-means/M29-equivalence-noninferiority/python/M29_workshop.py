from math import sqrt
from scipy.stats import norm,t

def tost(d,se,lo,hi,dist):
    p=(dist.sf((d-lo)/se),dist.cdf((d-hi)/se))
    h=dist.ppf(.95)*se
    return (*p,max(p),d-h,d+h)

print("L1:", -2 < -1.1 and 1.3 < 2)
print("L2:",tost(.4,.6,-2,2,t(38)))
se=sqrt(.45*.55/200+.42*.58/200)
print("L3:",tost(.45-.42,se,-.12,.12,norm))
