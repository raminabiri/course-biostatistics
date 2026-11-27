d <- read.csv("data/M57_time.csv")
fit <- survival::survdiff(survival::Surv(time,event)~group,d,rho=0)
print(c(O=fit$obs[1],E=fit$exp[1],V=fit$var[1,1],chisq=fit$chisq,
        p=pchisq(fit$chisq,1,lower.tail=FALSE)))
stopifnot(abs(fit$chisq-.663)<.001)
