d <- read.csv("data/M61_design.csv")
normal <- with(d,2*(qnorm(1-alpha/2)+qnorm(power))^2*(sd/difference)^2)
exact <- mapply(function(delta,sd,alpha,power)
  power.t.test(delta=delta,sd=sd,sig.level=alpha,power=power,strict=TRUE)$n,
  d$difference,d$sd,d$alpha,d$power)
print(cbind(normal,exact,ceil_normal=ceiling(normal),ceil_exact=ceiling(exact)))
stopifnot(all(ceiling(normal)==c(63,175)),ceiling(exact[1])==64)
