d <- read.csv("data/practice.csv")
a <- d$value[d$group=="A"]; b <- d$value[d$group=="B"]
w <- wilcox.test(a,b,exact=TRUE)
cat("L1:",w$statistic,w$p.value,"\n")
k <- ks.test(a,b,exact=TRUE); cat("L2:",k$statistic,k$p.value,"\n")
tab <- table(d$group,d$value>median(d$value))
cat("L3:",median(outer(a,b,"-")),fisher.test(tab)$p.value,"\n")
