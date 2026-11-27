GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=grp A1 value F8.2.
RECODE grp ('A'=1) ('B'=2) INTO group_id.
VALUE LABELS group_id 1 'A' 2 'B'.
NPAR TESTS /M-W=value BY group_id(1,2) /K-S=value BY group_id(1,2).
AGGREGATE OUTFILE=* MODE=ADDVARIABLES /median_all=MEDIAN(value).
COMPUTE above=(value>median_all).
CROSSTABS /TABLES=group_id BY above /STATISTICS=CHISQ /CELLS=COUNT.
MATRIX.
GET input /VARIABLES=group_id value /MISSING=OMIT.
COMPUTE n=NROW(input).
COMPUTE left=MAKE(n,1,0).
COMPUTE right=MAKE(n,1,0).
COMPUTE n1=0.
COMPUTE n2=0.
LOOP i=1 TO n.
  DO IF (input(i,1)=1).
    COMPUTE n1=n1+1.
    COMPUTE left(n1,1)=input(i,2).
  ELSE.
    COMPUTE n2=n2+1.
    COMPUTE right(n2,1)=input(i,2).
  END IF.
END LOOP.
COMPUTE diffs=MAKE(n1*n2,1,0).
LOOP i=1 TO n1.
  LOOP j=1 TO n2.
    COMPUTE diffs((i-1)*n2+j,1)=left(i,1)-right(j,1).
  END LOOP.
END LOOP.
COMPUTE sorted=GRADE(diffs).
COMPUTE ranks=MAKE(n1*n2,1,0).
LOOP i=1 TO n1*n2.
  COMPUTE ranks(sorted(i,1),1)=diffs(i,1).
END LOOP.
COMPUTE hl=(ranks(TRUNC((n1*n2+1)/2),1)+ranks(TRUNC(n1*n2/2)+1,1))/2.
PRINT hl /TITLE='Hodges-Lehmann estimate (A minus B)' /FORMAT='F12.6'.
END MATRIX.
