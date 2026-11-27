* The balanced classical time test can be reproduced with id and time as factors.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F3.0 group_id F1.0 time F1.0 condition F1.0 value F8.2.
SELECT IF condition=0.
GLM value BY id time /DESIGN=id time.
GET DATA /TYPE=TXT /FILE='data/wide.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F3.0 group_id F1.0 t0c0 F8.2 t0c1 F8.2 t1c0 F8.2 t1c1 F8.2 t2c0 F8.2 t2c1 F8.2.
T-TEST PAIRS=t1c0 t2c0 t2c0 WITH t0c0 t0c0 t1c0 (PAIRED) /CRITERIA=CI(.95).
