d <- read.csv("data/M74_L1.csv")
definitely <- with(d,lower>4 | (lower==4 & kind=="interval"))
possible <- d$upper>4
bounds <- c(mean(d$lower),mean(d$upper))
stopifnot(all(bounds==c(3.5,5.5)),mean(definitely)==.5,mean(possible)==.5)
print(c(lower=bounds[1],upper=bounds[2],GM_upper=exp(mean(log(d$upper))),above=mean(definitely)))
