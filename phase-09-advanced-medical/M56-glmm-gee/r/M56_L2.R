distance <- abs(outer(0:2,0:2,"-"))
models <- list(independent=diag(3),exchangeable=ifelse(distance==0,1,.4),AR1=.4^distance)
print(models)
stopifnot(abs(models$AR1[1,3]-.16)<1e-12)
if (requireNamespace("geepack",quietly=TRUE)) {
  d <- read.csv("data/M56_binary.csv")
  d <- d[order(d$id,d$time),]
  for (s in c("independence","exchangeable","ar1")) {
    fit <- geepack::geeglm(completed~group,data=d,id=id,waves=time,
                            family=binomial(),corstr=s)
    print(summary(fit)$coefficients)
  }
} else message("Optional geepack fits skipped; matrix calculations completed.")
