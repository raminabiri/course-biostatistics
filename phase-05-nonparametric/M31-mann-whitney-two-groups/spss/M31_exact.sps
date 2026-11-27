PRESERVE.
SET MXLOOPS=20000.
GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=grp A1 value F8.2.
RECODE grp ('A'=1) ('B'=2) INTO group_id.
VALUE LABELS group_id 1 'A' 2 'B'.
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

* Reference calculations for the complete, untied practice table.
COMPUTE order=GRADE(input(:,2)).
COMPUTE labels=MAKE(n,1,0).
LOOP i=1 TO n.
  COMPUTE labels(order(i,1),1)=(input(i,1)=1).
END LOOP.
COMPUTE observed_u=0.
COMPUTE observed_gap=0.
COMPUTE observed_above=0.
COMPUTE used_a=0.
COMPUTE used_b=0.
LOOP i=1 TO n.
  DO IF (labels(i,1)=1).
    COMPUTE used_a=used_a+1.
    COMPUTE observed_u=observed_u+used_b.
    DO IF (i>n/2).
      COMPUTE observed_above=observed_above+1.
    END IF.
  ELSE.
    COMPUTE used_b=used_b+1.
  END IF.
  COMPUTE separation=ABS(used_a*n2-used_b*n1).
  DO IF (separation>observed_gap).
    COMPUTE observed_gap=separation.
  END IF.
END LOOP.
COMPUTE total=0.
COMPUTE tail_u=0.
COMPUTE cutoff_u=observed_u.
DO IF (n1*n2-observed_u<cutoff_u).
  COMPUTE cutoff_u=n1*n2-observed_u.
END IF.
COMPUTE tail_ks=0.
COMPUTE above_counts=MAKE(n1+1,1,0).
COMPUTE mask_limit=(2**n)-1.
LOOP mask=0 TO mask_limit.
  COMPUTE remainder=mask.
  COMPUTE used_a=0.
  COMPUTE used_b=0.
  COMPUTE u=0.
  COMPUTE gap=0.
  COMPUTE above=0.
  LOOP i=1 TO n.
    COMPUTE bit=MOD(remainder,2).
    COMPUTE remainder=TRUNC(remainder/2).
    DO IF (bit=1).
      COMPUTE used_a=used_a+1.
      COMPUTE u=u+used_b.
      DO IF (i>n/2).
        COMPUTE above=above+1.
      END IF.
    ELSE.
      COMPUTE used_b=used_b+1.
    END IF.
    COMPUTE separation=ABS(used_a*n2-used_b*n1).
  DO IF (separation>gap).
    COMPUTE gap=separation.
  END IF.
  END LOOP.
  DO IF (used_a=n1).
    COMPUTE total=total+1.
    COMPUTE above_counts(above+1,1)=above_counts(above+1,1)+1.
    DO IF (u<=cutoff_u).
      COMPUTE tail_u=tail_u+1.
    END IF.
    DO IF (gap>=observed_gap).
      COMPUTE tail_ks=tail_ks+1.
    END IF.
  END IF.
END LOOP.
COMPUTE p_fisher=0.
LOOP i=1 TO n1+1.
  DO IF (above_counts(i,1)<=above_counts(observed_above+1,1)).
    COMPUTE p_fisher=p_fisher+above_counts(i,1)/total.
  END IF.
END LOOP.
COMPUTE p_u=2*tail_u/total.
DO IF (p_u>1).
  COMPUTE p_u=1.
END IF.
COMPUTE results={observed_u,p_u,observed_gap/(n1*n2),tail_ks/total,p_fisher}.
PRINT results /TITLE='U of A, exact MW p, KS D, conditional KS p, exact Fisher p' /FORMAT='F13.9'.
END MATRIX.
RESTORE.
