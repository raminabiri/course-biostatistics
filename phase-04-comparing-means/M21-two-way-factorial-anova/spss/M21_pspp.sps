GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=a F1.0 b F1.0 c F1.0 replicate F1.0 value F8.2.
TEMPORARY.
SELECT IF c=0.
GLM value BY a b /DESIGN=a b a*b.
GLM value BY a b c /DESIGN=a b c a*b a*c b*c a*b*c.
