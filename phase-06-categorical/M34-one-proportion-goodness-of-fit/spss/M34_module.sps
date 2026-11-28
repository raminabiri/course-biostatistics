* Run from the M34 folder or set the full path to the CSV file.
GET DATA /TYPE=TXT /FILE='data/M34_practice.csv'
 /DELCASE=LINE /DELIMITERS=',' /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F3.0 on_time F1.0 route A1.
FREQUENCIES VARIABLES=on_time route.
COMPUTE all_rows=1.
COMPUTE in_a=(route='A').
COMPUTE in_b=(route='B').
COMPUTE in_c=(route='C').
AGGREGATE /OUTFILE=* /BREAK=all_rows
 /n=N /k=SUM(on_time) /obs_a=SUM(in_a) /obs_b=SUM(in_b) /obs_c=SUM(in_c).
COMPUTE p0=.5.
COMPUTE estimate=k/n.
COMPUTE p_right=1-CDF.BINOM(k-1,n,p0).
COMPUTE observed_mass=PDF.BINOM(k,n,p0).
COMPUTE p_two=0.
PRESERVE.
SET MXLOOPS=1000.
LOOP #i=0 TO n.
 COMPUTE #mass=PDF.BINOM(#i,n,p0).
 IF (#mass<=observed_mass*(1+1E-12)) p_two=p_two+#mass.
END LOOP.
RESTORE.
COMPUTE z=(estimate-p0)/SQRT(p0*(1-p0)/n).
COMPUTE p_z=2*CDF.NORMAL(-ABS(z),0,1).
COMPUTE z_cc=MAX(0,(ABS(k-n*p0)-.5)/SQRT(n*p0*(1-p0))).
COMPUTE p_z_cc=2*CDF.NORMAL(-z_cc,0,1).
COMPUTE chi=(obs_a-.5*n)**2/(.5*n)+(obs_b-.3*n)**2/(.3*n)+(obs_c-.2*n)**2/(.2*n).
COMPUTE p_chi=1-CDF.CHISQ(chi,2).
FORMATS n k obs_a obs_b obs_c (F3.0)
 estimate p_right p_two z p_z p_z_cc chi p_chi (F10.6).
LIST n k estimate p_right p_two z p_z p_z_cc.
LIST obs_a obs_b obs_c chi p_chi.
