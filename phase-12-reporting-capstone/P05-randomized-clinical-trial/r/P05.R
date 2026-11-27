d<-read.csv("data/P05.csv",na.strings="")
summary_by_arm<-lapply(split(d$outcome,d$arm),function(x) c(n=length(x),k=sum(x==1,na.rm=TRUE),missing=sum(is.na(x))))
p<-summary_by_arm$program
c<-summary_by_arm$control
observed<-p["k"]/(p["n"]-p["missing"])-c["k"]/(c["n"]-c["missing"])
lo<-p["k"]/p["n"]-(c["k"]+c["missing"])/c["n"]
hi<-(p["k"]+p["missing"])/p["n"]-c["k"]/c["n"]
n<-ceiling((qnorm(.975)*sqrt(2*.525*.475)+qnorm(.8)*sqrt(.45*.55+.60*.40))^2/.15^2)
stopifnot(abs(lo-.08)<1e-12,abs(hi-.2)<1e-12,n==173)
print(summary_by_arm)
print(c(observed=unname(observed),lower=unname(lo),upper=unname(hi),planned_per_arm=n))
