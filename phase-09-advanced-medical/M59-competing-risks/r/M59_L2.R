library(survival)
d <- read.csv("data/M59_groups.csv")
d$status <- factor(d$status,levels=0:2)
expanded <- finegray(Surv(time,status)~group+id,data=d,etype="1")
fit <- coxph(Surv(fgstart,fgstop,fgstatus)~group+cluster(id),weights=fgwt,data=expanded)
out <- summary(survfit(Surv(time,status)~group,data=d),times=4)$pstate[,2]
print(out)
print(exp(coef(fit)))
stopifnot(max(abs(out-c(13/60,.3)))<1e-10,
          abs(coef(fit)[1]-.2781739)<1e-6)
if (requireNamespace("cmprsk",quietly=TRUE)) {
  print(cmprsk::cuminc(d$time,as.integer(d$status)-1,d$group,cencode=0)$Tests)
} else message("Gray test skipped: cmprsk unavailable.")
