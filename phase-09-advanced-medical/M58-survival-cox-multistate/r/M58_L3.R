d <- read.csv("data/M58_cox.csv")
rmst <- function(rows,tau) {
  s <- 1; previous <- 0; area <- 0
  for (t in sort(unique(rows$time[rows$event==1 & rows$time<tau]))) {
    area <- area+(t-previous)*s
    s <- s*(1-sum(rows$time==t & rows$event==1)/sum(rows$time>=t))
    previous <- t
  }
  area+(tau-previous)*s
}
out <- sapply(split(d,d$group),rmst,tau=5)
print(out)
print(exp(coef(survival::survreg(survival::Surv(time,event)~group,data=d,dist="weibull"))))
stopifnot(max(abs(out-c(3.4,4.4)))<1e-10)
