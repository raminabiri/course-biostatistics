GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=grp A1 value F8.2.
RECODE grp ('A'=1) ('B'=2) INTO group_id.
VALUE LABELS group_id 1 'A' 2 'B'.
NPAR TESTS /M-W=value BY group_id(1,2).
AGGREGATE OUTFILE=* MODE=ADDVARIABLES /median_all=MEDIAN(value).
COMPUTE above=(value>median_all).
CROSSTABS /TABLES=group_id BY above /CELLS=COUNT.
