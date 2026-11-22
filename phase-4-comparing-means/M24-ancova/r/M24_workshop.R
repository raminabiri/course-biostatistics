d <- read.csv("data/practice.csv")
d$baseline <- d$baseline-24
s <- subset(d,b==0)
fit <- lm(value~a+baseline,s)
cat("L1:",predict(fit,data.frame(a=0:1,baseline=0)),"\n")
cat("L2:\n"); print(anova(lm(value~a+b+baseline,d),lm(value~a*b+baseline,d)))
s$change <- 2 + 1.5*s$a + .3*s$baseline+c(-1,1,0,2,-2,1,0,1,-1,0,2,-1)
cat("L3:\n"); print(anova(lm(change~baseline,s),lm(change~baseline+a,s)))
