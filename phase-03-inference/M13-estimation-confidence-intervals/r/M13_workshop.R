mean_ci <- 50 + c(-1, 1) * qt(.975, 24) * 10 / sqrt(25)
exact_ci <- binom.test(2,20)$conf.int
v <- c(100/25,64/20)
df <- sum(v)^2 / sum(v^2 / c(24,19))
diff_ci <- 4 + c(-1,1) * qt(.975,df) * sqrt(sum(v))
stopifnot(abs(mean_ci[1]-45.87)<.01, abs(exact_ci[2]-.317)<.001, abs(diff_ci[2]-9.41)<.02)
cat("L1:", mean_ci, "\nL2:", exact_ci, "\nL3:", diff_ci, "\n")
