x <- c(pnorm(110,100,10),exp(log(10)),pexp(4,.25,lower.tail=FALSE),qt(.975,9))
stopifnot(max(abs(x-c(.8413447461,10,.3678794412,2.2621571629)))<1e-8)
print(x)
