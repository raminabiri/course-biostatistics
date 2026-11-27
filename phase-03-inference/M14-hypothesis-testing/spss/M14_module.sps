DATA LIST FREE / caseid.
BEGIN DATA
1
END DATA.
COMPUTE se0=10/SQRT(25).
COMPUTE t0=(104-100)/se0.
COMPUTE df=24.
COMPUTE p_two=2*CDF.T(-ABS(t0),df).
COMPUTE half_width=IDF.T(.975,df)*se0.
COMPUTE lower=104-half_width.
COMPUTE upper=104+half_width.
FORMATS se0 t0 df p_two lower upper (F12.6).
LIST VARIABLES=se0 t0 df p_two lower upper.
