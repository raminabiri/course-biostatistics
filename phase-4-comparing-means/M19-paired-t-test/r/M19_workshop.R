before <- c(47,50,51,53,55,56,59,61)
after <- c(45,46,48,49,50,52,54,57)
d <- after-before
fit <- t.test(after,before,paired=TRUE)
cat("L1:",mean(d),fit$statistic,"\nL2:",sd(d),sd(d)/sqrt(length(d)),
    "\nL3:",pt(fit$statistic,fit$parameter),fit$conf.int,"\n")
