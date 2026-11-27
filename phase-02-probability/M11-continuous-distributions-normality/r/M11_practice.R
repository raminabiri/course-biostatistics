cat("L1:", pnorm(130, 100, 15, lower.tail = FALSE), qnorm(.95, 100, 15), "\n")
cat("L2:", exp(log(10) + .5^2 / 2), pexp(1, 2, lower.tail = FALSE), "\n")
cat("L3:", qt(.975, 9), pchisq(5, 3), pf(2, 3, 7), "\n")
source("r/M11_qq.R")
