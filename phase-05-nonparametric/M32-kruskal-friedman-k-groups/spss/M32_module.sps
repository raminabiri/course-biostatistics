* Run from the M32 module folder, or edit these two file paths.
GET DATA /TYPE=TXT /FILE='data/independent.csv'
 /DELCASE=LINE /DELIMITERS=',' /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=group_id F1.0 value F8.2.
NPAR TESTS /K-W=value BY group_id(1,3).
* Optional IBM SPSS Premium / Exact Tests command, select and run separately.
* NPAR TESTS /J-T=value BY group_id(1,3).
GET DATA /TYPE=TXT /FILE='data/blocked_wide.csv'
 /DELCASE=LINE /DELIMITERS=',' /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=block_id F2.0 t1 F8.2 t2 F8.2 t3 F8.2.
NPAR TESTS /FRIEDMAN=t1 t2 t3 /KENDALL=t1 t2 t3.
