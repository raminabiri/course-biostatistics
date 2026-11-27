DATA LIST FREE / caseid.
BEGIN DATA
1
END DATA.
COMPUTE se0=10/SQRT(25).
COMPUTE hw=IDF.T(.975,24)*se0.
COMPUTE lower_t=100-hw.
COMPUTE upper_t=100+hw.
COMPUTE p=18/30.
COMPUTE z=IDF.NORMAL(.975,0,1).
COMPUTE middle=(p+z**2/60)/(1+z**2/30).
COMPUTE half_w=z*SQRT(p*(1-p)/30+z**2/3600)/(1+z**2/30).
COMPUTE lower_w=middle-half_w.
COMPUTE upper_w=middle+half_w.
COMPUTE difference=105-100.
COMPUTE se_diff=SQRT(8).
FORMATS se0 lower_t upper_t p lower_w upper_w difference se_diff (F12.6).
LIST VARIABLES=se0 lower_t upper_t p lower_w upper_w difference se_diff.
