DATA LIST FREE / caseid.
BEGIN DATA
1
END DATA.
COMPUTE avg=MEAN(2,-1,3).
COMPUTE std_error=SD(2,-1,3)/SQRT(3).
COMPUTE varratio=6**2/2**2.
COMPUTE allmean=MEAN(2,3,4,5,20).
COMPUTE case_mean=MEAN(2,3,4,5).
FORMATS avg std_error varratio allmean case_mean (F12.6).
LIST VARIABLES=avg std_error varratio allmean case_mean.
