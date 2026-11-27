DATA LIST FREE / caseid.
BEGIN DATA
1
END DATA.
COMPUTE rawdiff=105-100.
COMPUTE d=rawdiff/10.
COMPUTE ra=15/100.
COMPUTE rb=25/100.
COMPUTE arr=rb-ra.
COMPUTE rr=ra/rb.
COMPUTE nnt=1/arr.
COMPUTE multiplier=(5/2.5)**2.
FORMATS rawdiff d ra rb arr rr nnt multiplier (F12.6).
LIST VARIABLES=rawdiff d ra rb arr rr nnt multiplier.
