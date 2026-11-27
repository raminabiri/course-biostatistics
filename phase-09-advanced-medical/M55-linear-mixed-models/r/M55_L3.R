d <- read.csv("data/M55_clusters.csv")
fit <- nlme::lme(y~group,random=~1|class_id,data=d)
t <- summary(fit)$tTable
print(t)
print(nlme::VarCorr(fit))
stopifnot(abs(t["groupB","Value"]-2)<1e-8,
          abs(t["groupB","Std.Error"]-sqrt(8))<3e-5)
