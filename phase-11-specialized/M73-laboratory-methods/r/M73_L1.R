d <- read.csv("data/M73_L1.csv")
fit <- lm(signal~x,d)
a <- coef(fit)[1]
b <- coef(fit)[2]
results <- c(slope=unname(b), unknown=unname((12.5-a)/b), LOD=unname(3.3*.3/b), LOQ=unname(10*.3/b))
stopifnot(max(abs(results-c(3,3.5,.33,1)))<1e-12)
print(results)
