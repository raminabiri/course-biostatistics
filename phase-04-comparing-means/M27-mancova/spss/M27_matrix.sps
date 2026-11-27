GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=a F1.0 b F1.0 replicate F2.0 baseline F8.2 y F8.2 z F8.2 y0 F8.2 z0 F8.2.
COMPUTE x=baseline-25.
MATRIX.
GET input /VARIABLES=a b x y z /MISSING=OMIT.
COMPUTE n=NROW(input).
COMPUTE n0=n-CSUM(input(:,2)).
COMPUTE b0=MAKE(n0,5,0).
COMPUTE k=0.
LOOP i=1 TO n.
  DO IF (input(i,2)=0).
    COMPUTE k=k+1.
    COMPUTE b0(k,:)=input(i,:).
  END IF.
END LOOP.
COMPUTE ones=MAKE(n,1,1).
COMPUTE a=input(:,1).
COMPUTE b=input(:,2).
COMPUTE x=input(:,3).
COMPUTE additive={ones,a,b,x}.
COMPUTE common={additive,a&*b}.
COMPUTE out=MAKE(3,6,0).
LOOP case_no=1 TO 3.
  DO IF (case_no=1).
    COMPUTE small={MAKE(n0,1,1),b0(:,3)}.
    COMPUTE large={small,b0(:,1)}.
    COMPUTE response=b0(:,4:5).
  ELSE IF (case_no=2).
    COMPUTE small=additive.
    COMPUTE large=common.
    COMPUTE response=input(:,4:5).
  ELSE.
    COMPUTE small=common.
    COMPUTE large={common,a&*x}.
    COMPUTE response=input(:,4:5).
  END IF.
  COMPUTE coef0=INV(SSCP(small))*T(small)*response.
  COMPUTE coef1=INV(SSCP(large))*T(large)*response.
  DO IF (case_no=1).
    COMPUTE predictions={1,0,0;1,0,1}*coef1.
    PRINT predictions /TITLE='Baseline 25: y and z for A0 and A1' /FORMAT='F12.6'.
  END IF.
  COMPUTE e0=SSCP(response-small*coef0).
  COMPUTE e1=SSCP(response-large*coef1).
  COMPUTE h=e0-e1.
  COMPUTE root=TRACE(INV(e1)*h).
  COMPUTE df2=NROW(response)-NCOL(large)-1.
  COMPUTE f_value=root*df2/2.
  COMPUTE p=EXP((df2/2)*LN(df2/(df2+2*f_value))).
  COMPUTE out(case_no,:)={root/(1+root),1/(1+root),f_value,2,df2,p}.
END LOOP.
PRINT out /TITLE='Adjusted A, A by B, slopes: Pillai, Wilks, F, df1, df2, p' /FORMAT='E16.8'.
END MATRIX.
