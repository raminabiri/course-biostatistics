DATA LIST FREE / patient_id day age ward (A8) temperature.
BEGIN DATA
1 0 24 internal 36.8
1 3 24 internal 37.0
2 0 51 surgery 37.2
2 3 51 surgery .
3 0 38 internal 38.1
3 3 38 internal 37.4
END DATA.
COMPUTE valid=NOT MISSING(temperature).
AGGREGATE OUTFILE=* /BREAK=day /rows=N /valid_n=SUM(valid) /average=MEAN(temperature).
FORMATS average (F8.4).
LIST VARIABLES=day rows valid_n average.
