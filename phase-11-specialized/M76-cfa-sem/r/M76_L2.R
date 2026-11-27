d<-read.csv("data/M76_L2.csv",row.names=1)
s<-as.matrix(d)
load3<-function(m) { x<-sqrt(m[1,2]*m[1,3]/m[2,3]); c(x,m[1,2]/x,m[1,3]/x) }
f<-load3(s[1:3,1:3])
a<-load3(s[4:6,4:6])
cross<-outer(f,a)
phi<-mean(s[1:3,4:6]/cross)
stopifnot(abs(phi-.35)<1e-12,max(abs(s[1:3,4:6]-phi*cross))<1e-12)
print(list(f=f,a=a,phi=phi))
if(requireNamespace("lavaan",quietly=TRUE)){
 model<-"fatigue =~ f1 + f2 + f3
activity =~ a1 + a2 + a3"
 fit<-lavaan::cfa(model,sample.cov=s,sample.nobs=200,std.lv=TRUE,sample.cov.rescale=FALSE)
 stopifnot(lavaan::lavInspect(fit,"converged"))
 print(lavaan::lavInspect(fit,"cor.lv"))
}
