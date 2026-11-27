p <- c(dbinom(2,5,.2), dpois(3,2), dnbinom(3,2,.4), dhyper(2,5,15,4))
stopifnot(isTRUE(all.equal(p,c(.2048,4/3*exp(-2),.13824,1050/4845))))
print(p)
