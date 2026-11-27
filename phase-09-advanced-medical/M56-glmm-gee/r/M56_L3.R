d <- read.csv("data/M56_counts.csv")
fit <- glm(events~group+offset(log(exposure)),data=d,family=poisson())
x <- model.matrix(fit)
mu <- fitted(fit)
bread <- solve(crossprod(x,x*as.vector(mu)))
scores <- rowsum(x*as.vector(d$events-mu),d$id)
v <- bread %*% crossprod(scores) %*% bread
print(c(IRR=unname(exp(coef(fit)[2])),robust_se=sqrt(v[2,2])))
stopifnot(abs(exp(coef(fit)[2])-2)<1e-8)
