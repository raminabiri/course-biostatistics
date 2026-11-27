d <- read.csv("data/M57_time.csv")
m <- t(sapply(sort(unique(d$time[d$event==1])),function(time) {
  risk <- d[d$time>=time,]
  n <- nrow(risk); p <- mean(risk$group=="A")
  e <- d[d$time==time & d$event==1,]
  k <- nrow(e)
  c(n=n,U=sum(e$group=="A")-k*p,V=if(n>1) k*p*(1-p)*(n-k)/(n-1) else 0)
}))
w <- cbind(logrank=1,breslow=m[,"n"],tarone=sqrt(m[,"n"]))
stat <- colSums(w*m[,"U"])^2/colSums(w^2*m[,"V"])
print(rbind(chisq=stat,p=pchisq(stat,1,lower.tail=FALSE)))
stopifnot(abs(stat["logrank"]-.663280189)<1e-8)
