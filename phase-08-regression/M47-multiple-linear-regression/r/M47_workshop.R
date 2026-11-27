d <- read.csv("data/M47_practice.csv")
stopifnot(nrow(d)==60,!anyDuplicated(d$id))
d$h <- d$hours-9
d$group <- relevel(factor(d$group),ref="A")
m <- lm(score~h*group+prior,d)
print(coef(lm(score~h,d)))
print(coef(lm(score~h+prior+group,d)))
print(summary(m)$coefficients)
x <- model.matrix(m)[,-1]
vif <- sapply(seq_len(ncol(x)),function(j) 1/(1-summary(lm(x[,j]~x[,-j]))$r.squared))
names(vif) <- colnames(x)
print(vif)
i <- which.max(cooks.distance(m))
cat("L3:",d$id[i],residuals(m)[i],hatvalues(m)[i],cooks.distance(m)[i],"\n")
sensitivity <- coef(lm(score~h*group+prior,d[d$id!=60,]))["h:groupB"]
print(sensitivity)
stopifnot(d$id[i]==60,abs(sensitivity-.3629957)<1e-7)
