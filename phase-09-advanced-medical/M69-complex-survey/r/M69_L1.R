d <- read.csv("data/M69_L1.csv")
estimate <- weighted.mean(d$y,d$weight)
d$linearized <- d$weight*(d$y-estimate)
psu <- aggregate(linearized~stratum+psu,d,sum)
squared <- tapply(psu$linearized,psu$stratum,function(x) diff(x)^2)
v <- sum(squared)/sum(d$weight)^2
regression <- coef(lm(y~stratum,data=d,weights=weight))
stopifnot(estimate==.375,v==10/256,abs(regression[2]+.5)<1e-12)
print(c(prevalence=estimate,SE=sqrt(v),DEFF_example=v/.025,regression))
