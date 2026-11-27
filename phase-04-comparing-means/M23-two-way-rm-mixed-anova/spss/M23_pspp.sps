GET DATA /TYPE=TXT /FILE='data/wide.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F3.0 group_id F1.0 t0c0 F8.2 t0c1 F8.2 t1c0 F8.2 t1c1 F8.2 t2c0 F8.2 t2c1 F8.2.
COMPUTE change=t2c0-t0c0.
T-TEST GROUPS=group_id(1,0) /VARIABLES=change /CRITERIA=CI(.95).
GET DATA /TYPE=TXT /FILE='data/condition-differences.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=id F3.0 time F1.0 difference F8.2.
GLM difference BY id time /DESIGN=id time.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F3.0 group_id F1.0 time F1.0 condition F1.0 value F8.2.
SELECT IF condition=0.
GLM value BY id time group_id /DESIGN=id time time*group_id.
