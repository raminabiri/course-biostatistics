d <- read.csv("data/M57_time.csv")
s <- summary(survival::survfit(survival::Surv(time,event)~group,d))
print(data.frame(group=s$strata,time=s$time,risk=s$n.risk,events=s$n.event,survival=s$surv))
stopifnot(max(abs(s$surv-c(.8,8/15,4/15,.8,.4)))<1e-12)
