DATA LIST FREE / ref_k ref_n cmp_k cmp_n x1 x2 x3 a b c d.
BEGIN DATA
24 200 8 100 3 5 10 12 288 9 291
END DATA.
COMPUTE ref_risk=ref_k/ref_n.
COMPUTE cmp_risk=cmp_k/cmp_n.
COMPUTE diff_pp=100*(ref_risk-cmp_risk).
COMPUTE rel_pct=diff_pp/ref_risk.
COMPUTE inc100=8/160*100.
COMPUTE x_mean=MEAN(x1,x2,x3).
COMPUTE sqsum=x1**2+x2**2+x3**2.
COMPUTE sumsq=SUM(x1,x2,x3)**2.
COMPUTE row2=c+d.
COMPUTE col1=a+c.
COMPUTE linear3=80-20*3.
COMPUTE exp3=80*.5**3.
COMPUTE logratio=LN(exp3/80)/LN(2).
FORMATS diff_pp rel_pct inc100 x_mean sqsum sumsq row2 col1 linear3 exp3 logratio (F8.4).
LIST VARIABLES=diff_pp rel_pct inc100 x_mean sqsum sumsq row2 col1 linear3 exp3 logratio.
