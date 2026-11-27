d <- read.csv("data/M62_pool.csv")
m <- nrow(d)
within <- mean(d$within_variance)
between <- var(d$estimate)
extra <- (1 + 1 / m) * between
total <- within + extra
df <- (m - 1) * (1 + within / extra)^2
stopifnot(isTRUE(all.equal(total, 16/3)), isTRUE(all.equal(df, 32)))
print(c(estimate = mean(d$estimate), within = within, between = between,
        total = total, SE = sqrt(total), df = df))
