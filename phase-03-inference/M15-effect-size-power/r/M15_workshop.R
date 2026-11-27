d <- (54-50)/8
g <- (1-3/(4*38-1))*d
rd <- 30/100-20/100
rr <- (30/100)/(20/100)
or <- (30/70)/(20/80)
n <- ceiling(power.t.test(delta=.5, sd=1, power=.8,
                         type="two.sample", alternative="two.sided", strict=TRUE)$n)
stopifnot(n==64, abs(or-12/7)<1e-9)
cat("L1:",d,g,"\nL2:",rd,rr,or,"\nL3:",n,"per group\n")
