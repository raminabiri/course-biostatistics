cat("L1:", dbinom(2, 5, .2), pbinom(1, 5, .2, lower.tail = FALSE), "\n")
cat("L2:", dpois(0, 2), dnbinom(1, 2, .5), "\n")
cat("L3:", dhyper(2, 3, 7, 4), "\n")
