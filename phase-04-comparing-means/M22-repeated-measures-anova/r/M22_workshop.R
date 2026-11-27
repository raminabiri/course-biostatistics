long <- read.csv("data/practice.csv")
data <- subset(long, condition == 0)
data$id <- factor(data$id)
data$time <- factor(data$time)

counts <- xtabs(~ id + time, data)
stopifnot(all(counts == 1), !anyNA(data$value))
model <- aov(value ~ time + Error(id / time), data = data)
cat("L1: Time\n")
print(summary(model))

wide <- xtabs(value ~ id + time, data)
n <- nrow(wide)
k <- ncol(wide)
subject_mean <- rowMeans(wide)
time_mean <- colMeans(wide)
overall_mean <- mean(wide)
residual <- sweep(sweep(wide, 1, subject_mean), 2, time_mean) + overall_mean
df_time <- k - 1
df_error <- (n - 1) * df_time
f_value <- (n * sum((time_mean - overall_mean)^2) / df_time) /
  (sum(residual^2) / df_error)

u <- (wide[, 1] - wide[, 2]) / sqrt(2)
v <- (wide[, 1] + wide[, 2] - 2 * wide[, 3]) / sqrt(6)
s <- cov(cbind(u, v))
epsilon <- sum(diag(s))^2 / (df_time * sum(s^2))
cat("L2: GG:", epsilon, df_time * epsilon, df_error * epsilon,
    pf(f_value, df_time * epsilon, df_error * epsilon, lower.tail = FALSE), "\n")

pairs <- list("T1-T0" = c(2, 1), "T2-T0" = c(3, 1), "T2-T1" = c(3, 2))
results <- lapply(pairs, function(i) t.test(wide[, i[1]], wide[, i[2]], paired = TRUE))
p <- vapply(results, function(fit) fit$p.value, numeric(1))
cat("L3: paired comparisons\n")
print(data.frame(p_raw = p, p_holm = p.adjust(p, "holm")))
print(results[["T2-T0"]])
