DATA LIST FREE / pid ldl.
BEGIN DATA
1 110
1 130
2 140
END DATA.
AGGREGATE OUTFILE=* /BREAK=pid /meanldl=MEAN(ldl).
DATASET NAME labs.
SORT CASES BY pid.
DATASET DECLARE registry.
DATASET ACTIVATE registry.
DATA LIST FREE / pid (F5.0) height_raw (F8.2) weight_kg (F8.2) sbp_raw (F5.0) smoker (A3).
BEGIN DATA
1 166 59 156 no
2 1.68 73.5 138 yes
3 153 62.2 -99 " "
END DATA.
COMPUTE height_cm=height_raw.
IF (pid=2) height_cm=100*height_raw.
RECODE sbp_raw (-99=SYSMIS) (ELSE=COPY) INTO sbp.
COMPUTE bmi=weight_kg/((height_cm/100)**2).
SORT CASES BY pid.
MATCH FILES /FILE=* /TABLE=labs /BY pid.
FORMATS height_cm sbp bmi meanldl (F8.2).
LIST VARIABLES=pid height_cm sbp smoker bmi meanldl.
