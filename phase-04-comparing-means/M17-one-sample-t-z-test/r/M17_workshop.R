# Run from the M17 directory. Base R is sufficient.
data <- read.csv("data/values.csv")
x <- data$value
stopifnot(is.numeric(x), length(x) == 8L, all(is.finite(x)))

target <- 50
sigma <- 8
n <- length(x)
delta <- mean(x) - target
se <- sd(x) / sqrt(n)
fit <- t.test(x, mu = target)

# L1: SD describes individuals. SE describes the sample mean.
print(c(n = n, mean = mean(x), sd = sd(x), se = se))
print(c(t = unname(fit$statistic), df = unname(fit$parameter), p_two = fit$p.value))

# L2: sigma is an assumption supplied by the exercise.
z <- delta / (sigma / sqrt(n))
print(c(z = z, pz_right = pnorm(z, lower.tail = FALSE),
        pz_two = 2 * pnorm(-abs(z))))

# L3: use the sign of t for the one-sided probabilities.
right <- pt(fit$statistic, fit$parameter, lower.tail = FALSE)
left <- pt(fit$statistic, fit$parameter)
print(c(pt_right = unname(right), pt_left = unname(left)))
print(rbind(mean_ci = fit$conf.int, difference_ci = fit$conf.int - target))
