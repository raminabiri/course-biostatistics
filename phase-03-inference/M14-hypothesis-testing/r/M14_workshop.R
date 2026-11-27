mean_value <- 54
target <- 50
se <- 10 / sqrt(25)
df <- 24
tval <- (mean_value - target) / se
right <- pt(tval, df, lower.tail = FALSE)
two <- 2 * pt(abs(tval), df, lower.tail = FALSE)
ci <- (mean_value-target) + c(-1,1)*qt(.975,df)*se
stopifnot(tval == 2, abs(two-.05694)<.0001, ci[1]<0, ci[2]>0)
cat("L1:", tval, df, "\nL2:", right, two, "\nL3:", ci, "\n")
