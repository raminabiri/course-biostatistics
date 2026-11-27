d <- read.csv("data/M55_repeated.csv")
d$t <- d$time-1
fit <- nlme::lme(y~t,random=list(id=nlme::pdDiag(~t)),data=d)
print(nlme::fixef(fit))
print(nlme::VarCorr(fit))
stopifnot(abs(nlme::fixef(fit)[2]-23/12)<1e-8,
          as.numeric(nlme::VarCorr(fit)["t","Variance"])<1e-5)
