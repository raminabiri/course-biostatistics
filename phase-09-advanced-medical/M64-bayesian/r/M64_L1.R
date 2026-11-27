d <- read.csv("data/M64_response.csv")
a <- d$prior_a + d$responded
b <- d$prior_b + d$total - d$responded
interval <- qbeta(c(.025, .975), a, b)
stopifnot(a == 9, b == 5, abs(a / (a + b) - 9/14) < 1e-12,
          all(abs(pbeta(interval, a, b) - c(.025, .975)) < 1e-12))
print(c(a = a, b = b, mean = a/(a+b), lower = interval[1], upper = interval[2]))
x <- seq(0, 1, by = .01)
write.csv(data.frame(probability = x, prior = dbeta(x, d$prior_a, d$prior_b),
                     posterior = dbeta(x, a, b)),
          "data/M64_densities.csv", row.names = FALSE)
