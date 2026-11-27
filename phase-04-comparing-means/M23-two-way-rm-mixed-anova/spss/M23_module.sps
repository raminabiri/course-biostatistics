GET DATA /TYPE=TXT /FILE='data/wide.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F3.0 group_id F1.0 t0c0 F8.2 t0c1 F8.2 t1c0 F8.2 t1c1 F8.2 t2c0 F8.2 t2c1 F8.2.
GLM t0c0 t0c1 t1c0 t1c1 t2c0 t2c1
 /WSFACTOR=time 3 Polynomial condition 2 Polynomial
 /PRINT=DESCRIPTIVE
 /WSDESIGN=time condition time*condition.
GLM t0c0 t1c0 t2c0 BY group_id
 /WSFACTOR=time 3 Polynomial
 /PRINT=DESCRIPTIVE
 /WSDESIGN=time
 /DESIGN=group_id.
COMPUTE change=t2c0-t0c0.
T-TEST GROUPS=group_id(1,0) /VARIABLES=change /CRITERIA=CI(.95).
