d <- read.csv("data/M56_binary.csv")
fit <- glm(completed~group,data=d,family=binomial())
x <- model.matrix(fit)
p <- fitted(fit)
bread <- solve(crossprod(x,x*as.vector(p*(1-p))))
scores <- rowsum(x*as.vector(d$completed-p),d$id)
covariance <- bread %*% crossprod(scores) %*% bread
print(c(OR=unname(exp(coef(fit)[2])),robust_se=sqrt(covariance[2,2])))
stopifnot(abs(exp(coef(fit)[2])-10/3)<1e-8)
