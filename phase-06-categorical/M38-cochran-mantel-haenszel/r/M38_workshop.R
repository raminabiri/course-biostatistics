d <- read.csv("data/M38_practice.csv")
stopifnot(nrow(d)==240, !anyDuplicated(d$id))
tab <- with(d,table(factor(group,levels=c("A","B")),
                    factor(success,levels=c(1,0)),stratum))
print(with(d,tapply(success,list(group,stratum),mean)))
print(with(d,tapply(success,group,mean)))
cmh <- mantelhaen.test(tab,correct=FALSE)
theta <- unname(cmh$estimate)
cat("L2:",theta,cmh$statistic,cmh$p.value,"\n")
parts <- apply(tab,3,function(t) {
  n <- sum(t); r <- sum(t[1,]); m <- sum(t[,1])
  x <- uniroot(function(x) x*(n-r-m+x)-theta*(r-x)*(m-x),
               c(max(0,r+m-n),min(r,m)),tol=1e-12)$root
  fitted <- c(x,r-x,m-x,n-r-m+x)
  (t[1,1]-x)^2*sum(1/fitted)
})
bd <- sum(parts)
cat("L3:",bd,pchisq(bd,length(parts)-1,lower.tail=FALSE),"\n")
stopifnot(abs(theta-.7260273973)<1e-9,abs(bd-.2124803146)<1e-9)
