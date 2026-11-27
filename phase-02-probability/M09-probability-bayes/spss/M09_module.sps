GET DATA /TYPE=TXT /FILE='data/M09_individuals.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=id F6.0 population A8 reference A8 test A8 joint_code F1.0.
COMPUTE true_pos=(joint_code=1).
COMPUTE ref_pos=ANY(joint_code,1,2).
COMPUTE test_pos=ANY(joint_code,1,3).
COMPUTE union_pos=(joint_code<>4).
AGGREGATE OUTFILE=* /BREAK=population /n=N /tp=SUM(true_pos) /rp=SUM(ref_pos) /sp=SUM(test_pos) /un=SUM(union_pos).
COMPUTE sensitivity=tp/rp.
COMPUTE ppv=tp/sp.
COMPUTE union_probability=un/n.
FORMATS sensitivity ppv union_probability (F8.4).
LIST VARIABLES=population n tp rp sp sensitivity ppv union_probability.
