data <- read.csv("data/practice.csv")
after <- as.matrix(data[c("y", "z")])
before <- as.matrix(data[c("y0", "z0")])
test <- function(delta, covariance, weight, df_covariance, df_f) {
  p <- length(delta)
  t_squared <- weight * drop(crossprod(delta, solve(covariance, delta)))
  f_value <- t_squared * df_f / (p * df_covariance)
  c(T2=t_squared, F=f_value, p=pf(f_value, p, df_f, lower.tail=FALSE))
}
one_sample <- function(values, reference) {
  n <- nrow(values)
  test(colMeans(values)-reference, cov(values), n, n-1, n-ncol(values))
}
left <- after[data$a==0, ]
right <- after[data$a==1, ]
n0 <- nrow(left)
n1 <- nrow(right)
n <- n0+n1
pooled <- ((n0-1)*cov(left)+(n1-1)*cov(right))/(n-2)
cat("L1:", one_sample(left, c(47,27)), "\n")
cat("L2:", test(colMeans(right)-colMeans(left), pooled, n0*n1/n, n-2, n-3), "\n")
change <- after-before
cat("L3:", one_sample(change, c(0,0)), "\n")
p <- ncol(change)
factor <- p*(n-1)/(n-p)*qf(.95,p,n-p)
margin <- sqrt(factor*diag(cov(change))/n)
print(rbind(lower=colMeans(change)-margin, upper=colMeans(change)+margin))
