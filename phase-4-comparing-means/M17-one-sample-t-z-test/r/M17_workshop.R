x <- c(47,50,51,53,55,56,59,61)
fit <- t.test(x, mu=50)
z <- (mean(x)-50)/(8/sqrt(length(x)))
cat("L1:",fit$statistic,fit$p.value,"\nL2:",z,pnorm(z,lower.tail=FALSE),"\nL3:",fit$conf.int-50,"\n")
