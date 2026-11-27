* Open in a new SPSS session and select Run > All.
DATA LIST FREE /value.
BEGIN DATA
47
50
51
53
55
56
59
61
END DATA.
DATASET NAME M17Raw.
T-TEST
 /TESTVAL=50
 /MISSING=ANALYSIS
 /VARIABLES=value
 /CRITERIA=CI(.95).

* Generate one summary row while keeping the original data.
DATASET COPY M17Summary.
DATASET ACTIVATE M17Summary.
AGGREGATE
 /OUTFILE=*
 /n_valid=N(value)
 /mean_value=MEAN(value)
 /sd_value=SD(value).
COMPUTE delta=mean_value-50.
COMPUTE se_t=sd_value/SQRT(n_valid).
COMPUTE stat_t=delta/se_t.
COMPUTE df_t=n_valid-1.
COMPUTE pt_right=1-CDF.T(stat_t,df_t).
COMPUTE pt_left=CDF.T(stat_t,df_t).
COMPUTE pt_two=2*(1-CDF.T(ABS(stat_t),df_t)).
COMPUTE z_known=delta/(8/SQRT(n_valid)).
COMPUTE pz_right=1-CDF.NORMAL(z_known,0,1).
COMPUTE pz_two=2*(1-CDF.NORMAL(ABS(z_known),0,1)).
COMPUTE ci_lo=delta-IDF.T(.975,df_t)*se_t.
COMPUTE ci_hi=delta+IDF.T(.975,df_t)*se_t.
FORMATS delta se_t stat_t pt_right pt_left pt_two z_known pz_right pz_two ci_lo ci_hi (F12.6).
LIST VARIABLES=n_valid mean_value sd_value delta se_t stat_t df_t pt_two z_known pz_right pz_two pt_right pt_left ci_lo ci_hi.
