GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=a F1.0 b F1.0 replicate F2.0 baseline F8.2 y F8.2 z F8.2 y0 F8.2 z0 F8.2.
MATRIX.
GET input /VARIABLES=a b y z y0 z0 /MISSING=OMIT.
COMPUTE n=NROW(input).
COMPUTE ones=MAKE(n,1,1).
COMPUTE a=input(:,1).
COMPUTE b=input(:,2).
COMPUTE interaction=a&*b.
COMPUTE out=MAKE(3,8,0).
LOOP case_no=1 TO 3.
  COMPUTE response=input(:,3:4).
  DO IF (case_no=2).
    COMPUTE reduced={ones,a,b}.
    COMPUTE full={ones,a,b,interaction}.
  ELSE.
    COMPUTE reduced=ones.
    COMPUTE full={ones,a}.
  END IF.
  DO IF (case_no=3).
    COMPUTE response=response-input(:,5:6).
  END IF.
  COMPUTE coef0=INV(SSCP(reduced))*T(reduced)*response.
  COMPUTE coef1=INV(SSCP(full))*T(full)*response.
  COMPUTE e0=SSCP(response-reduced*coef0).
  COMPUTE e1=SSCP(response-full*coef1).
  COMPUTE h=e0-e1.
  COMPUTE root=TRACE(INV(e1)*h).
  COMPUTE df2=n-NCOL(full)-1.
  COMPUTE f_value=root*df2/2.
  COMPUTE p=EXP((df2/2)*LN(df2/(df2+2*f_value))).
  COMPUTE out(case_no,:)={root/(1+root),1/(1+root),root,root,f_value,2,df2,p}.
END LOOP.
PRINT out /TITLE='End group, interaction, change: Pillai, Wilks, HL, Roy, F, df1, df2, p' /FORMAT='E16.8'.
END MATRIX.
