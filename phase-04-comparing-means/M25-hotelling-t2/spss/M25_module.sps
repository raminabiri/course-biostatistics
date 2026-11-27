GET DATA /TYPE=TXT /FILE='data/practice.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=a F1.0 b F1.0 replicate F2.0 baseline F8.2 y F8.2 z F8.2 y0 F8.2 z0 F8.2.
MATRIX.
GET input /VARIABLES=a y z y0 z0 /MISSING=OMIT.
COMPUTE n=NROW(input).
COMPUTE n1=CSUM(input(:,1)).
COMPUTE n0=n-n1.
COMPUTE group0=MAKE(n0,2,0).
COMPUTE group1=MAKE(n1,2,0).
COMPUTE i0=0.
COMPUTE i1=0.
LOOP i=1 TO n.
  DO IF (input(i,1)=0).
    COMPUTE i0=i0+1.
    COMPUTE group0(i0,:)=input(i,2:3).
  ELSE.
    COMPUTE i1=i1+1.
    COMPUTE group1(i1,:)=input(i,2:3).
  END IF.
END LOOP.
COMPUTE change=input(:,2:3)-input(:,4:5).
COMPUTE mean0=CSUM(group0)/n0.
COMPUTE mean1=CSUM(group1)/n1.
COMPUTE delta=CSUM(change)/n.
COMPUTE s0=(SSCP(group0)-n0*T(mean0)*mean0)/(n0-1).
COMPUTE s1=(SSCP(group1)-n1*T(mean1)*mean1)/(n1-1).
COMPUTE sd=(SSCP(change)-n*T(delta)*delta)/(n-1).
COMPUTE pooled=((n0-1)*s0+(n1-1)*s1)/(n-2).
COMPUTE d0=mean0-{47,27}.
COMPUTE d1=mean1-mean0.
COMPUTE t_one=n0*d0*INV(s0)*T(d0).
COMPUTE t_two=(n0*n1/n)*d1*INV(pooled)*T(d1).
COMPUTE t_paired=n*delta*INV(sd)*T(delta).
COMPUTE f_one=t_one*(n0-2)/(2*(n0-1)).
COMPUTE f_two=t_two*(n-3)/(2*(n-2)).
COMPUTE f_paired=t_paired*(n-2)/(2*(n-1)).
COMPUTE p_one=1-FCDF(f_one,2,n0-2).
COMPUTE p_two=1-FCDF(f_two,2,n-3).
COMPUTE p_paired=1-FCDF(f_paired,2,n-2).
COMPUTE output={t_one,f_one,p_one;t_two,f_two,p_two;t_paired,f_paired,p_paired}.
PRINT output /TITLE='One sample, two groups, paired: T square, F, right-tail p' /FORMAT='E17.9'.
END MATRIX.
