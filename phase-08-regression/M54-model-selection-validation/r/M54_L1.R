d <- read.csv("data/M54_models.csv")
d$AIC <- -2*d$loglik+2*d$k
d$BIC <- -2*d$loglik+log(d$n)*d$k
print(d)
stopifnot(d$model[which.min(d$AIC)]=="B",d$model[which.min(d$BIC)]=="A")
