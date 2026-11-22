x <- read.csv("data/M16_groups.csv")
a <- x$A
b <- x$B
sw <- shapiro.test(a)
dev <- c(abs(a-median(a)), abs(b-median(b)))
groups <- rep(c("A","B"), lengths(list(a,b)))
bf <- summary(aov(dev ~ groups))[[1]]
bt <- bartlett.test(list(a,b))
n <- length(a)
grubbs <- max(abs(a-mean(a))) / sd(a)
tcrit <- qt(1-.05/(2*n), n-2)
cut <- (n-1)/sqrt(n)*sqrt(tcrit^2/(n-2+tcrit^2))
welch <- t.test(a,b,var.equal=FALSE)
stopifnot(abs(sw$p.value-.01404)<.0001,
          abs(bf[["Pr(>F)"]][1]-.26917)<.0001,
          grubbs>cut, abs(welch$p.value-.21865)<.0001)
cat("L1:", sw$statistic, sw$p.value, "\nL2:", bf[["F value"]][1], bf[["Pr(>F)"]][1], bt$p.value,
    "\nL3:", grubbs, cut, "\nL4:", welch$statistic, welch$p.value, "\n")

png("figures/M16_qq.png", width=1080, height=540, res=120)
par(mfrow=c(1,2))
qqnorm(a, pch=19, main="Group A")
qqline(a, col="#9c401a", lwd=2)
qqnorm(b, pch=19, main="Group B")
qqline(b, col="#9c401a", lwd=2)
dev.off()
