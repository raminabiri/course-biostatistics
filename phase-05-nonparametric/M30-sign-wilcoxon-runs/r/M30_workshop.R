d <- read.csv("data/practice.csv")
q <- subset(d,design=="paired")
x <- q$after-q$before
cat("L1:",binom.test(sum(x>0),sum(x!=0),alternative="less")$p.value,binom.test(sum(x>0),sum(x!=0))$p.value,"\n")
w <- wilcox.test(x,exact=TRUE)
cat("L2:",w$statistic,w$p.value,"\n")
seq <- subset(d,design=="runs")$before
count <- function(x) 1+sum(diff(x)!=0)
reference <- combn(length(seq),sum(seq),function(index) count(as.integer(seq_along(seq)%in%index)))
observed <- count(seq)
cat("L3:",observed,min(1,2*min(mean(reference<=observed),mean(reference>=observed))),"\n")
