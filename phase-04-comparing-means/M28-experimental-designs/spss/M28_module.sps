GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=design A8 u F2.0 v F2.0 w F2.0 period F1.0 value F16.8.
SELECT IF design='block'.
GLM value BY u w /DESIGN=u w.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=design A8 u F2.0 v F2.0 w F2.0 period F1.0 value F16.8.
SELECT IF design='latin'.
GLM value BY u v w /DESIGN=u v w.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=design A8 u F2.0 v F2.0 w F2.0 period F1.0 value F16.8.
SELECT IF design='nested'.
COMPUTE lab=10*u+v.
AGGREGATE /OUTFILE=* /BREAK=u lab /lab_mean=MEAN(value).
ONEWAY lab_mean BY u /STATISTICS DESCRIPTIVES.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=design A8 u F2.0 v F2.0 w F2.0 period F1.0 value F16.8.
SELECT IF design='cross'.
GLM value BY u period w /DESIGN=u period w.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=design A8 u F2.0 v F2.0 w F2.0 period F1.0 value F16.8.
SELECT IF design='nested'.
COMPUTE lab=10*u+v.
MIXED value BY u
 /FIXED=u | SSTYPE(3)
 /RANDOM=INTERCEPT | SUBJECT(lab) COVTYPE(VC)
 /METHOD=REML
 /PRINT=SOLUTION.
