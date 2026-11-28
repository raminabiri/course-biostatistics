d <- read.csv("data/M34_practice.csv")
n <- nrow(d)
k <- sum(d$on_time)
obs <- table(factor(d$route, levels=c("A","B","C")))
stopifnot(n == 100, k == 60, !anyDuplicated(d$id), all(obs == c(65,25,10)))
z <- (k/n-.5)/sqrt(.5*.5/n)
exact <- binom.test(k,n,.5)
gof <- chisq.test(obs,p=c(.5,.3,.2))
cat("L1:", binom.test(k,n,.5,alternative="greater")$p.value, exact$p.value, "\n")
cat("L2:", z, pnorm(z,lower.tail=FALSE), 2*pnorm(-abs(z)), "\n")
cat("L3:", gof$statistic, gof$parameter, gof$p.value, "\n")
stopifnot(abs(exact$p.value-.056887933641)<1e-10, abs(gof$statistic-31/3)<1e-10)

z_cc <- max(0, abs(k-n*.5)-.5)/sqrt(n*.5*.5)
cat("Corrected P:", 2*pnorm(-z_cc), "\n")
cat("95% exact interval:", exact$conf.int, "\n")
cat("95% Wilson interval:", prop.test(k,n,correct=FALSE)$conf.int, "\n")

# Enumerate counts with the Pearson statistic defining the tail.
p <- c(.5,.3,.2)
expected <- n*p
exact_gof <- 0
for (a in 0:n) {
  b <- 0:(n-a)
  c <- n-a-b
  chi <- (a-expected[1])^2/expected[1]+(b-expected[2])^2/expected[2]+(c-expected[3])^2/expected[3]
  joint_mass <- dbinom(a,n,p[1])*dbinom(b,n-a,p[2]/(1-p[1]))
  exact_gof <- exact_gof + sum(joint_mass[chi >= gof$statistic-1e-10])
}
cat("Exact multinomial Pearson tail:", exact_gof, "\n")
stopifnot(abs(exact_gof-.00586547283532)<1e-10)
