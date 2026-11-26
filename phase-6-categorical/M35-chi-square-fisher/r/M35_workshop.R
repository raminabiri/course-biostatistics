d <- read.csv("data/M35_practice.csv")
stopifnot(nrow(d)==150, !anyDuplicated(d$id))
large <- with(d,table(factor(group,levels=c("A","B","C")),
                      factor(response,levels=c("yes","partial","no"))))
binary <- cbind(large[1:2,1], rowSums(large[1:2,2:3]))
unadjusted <- chisq.test(binary,correct=FALSE)
yates <- chisq.test(binary,correct=TRUE)
z <- (.6-.4)/sqrt(.5*.5*(1/50+1/50))
cat("L1:", unadjusted$statistic, unadjusted$p.value, yates$statistic, yates$p.value,z,"\n")
fisher <- fisher.test(binary)
cat("L2 Fisher:", fisher$p.value,"\n")
r <- chisq.test(large)
e <- r$expected
positive <- large>0
g <- 2*sum(large[positive]*log(large[positive]/e[positive]))
small <- matrix(c(3,1,0,0,2,2,1,0,3),3,byrow=TRUE)
ffh <- fisher.test(small)$p.value
cat("L3:",r$statistic,r$p.value,g,pchisq(g,4,lower.tail=FALSE),r$stdres[1,1],ffh,"\n")
stopifnot(abs(unadjusted$statistic-z*z)<1e-12,abs(ffh-1/11)<1e-12)
