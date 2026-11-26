d <- read.csv("data/M42_two.csv")
tab <- with(d,table(rater_a,rater_b))
o <- tab/sum(tab)
e <- outer(rowSums(o),colSums(o))
gap <- abs(outer(0:2,0:2,"-"))/2
kappa <- function(w) {
  observed <- sum(o*w); expected <- sum(e*w)
  c(observed=observed,expected=expected,kappa=(observed-expected)/(1-expected))
}
print(rbind(simple=kappa(diag(3)),linear=kappa(1-gap),quadratic=kappa(1-gap^2)))
d <- read.csv("data/M42_multiple.csv")
scores <- as.matrix(d[c("rater_a","rater_b","rater_c")])
v <- sapply(0:2,function(level) rowSums(scores==level))
p <- colSums(v)/sum(v)
a <- mean(rowSums(v*(v-1))/6)
cf <- sum(p^2); cg <- sum(p*(1-p))/2
cat("L3:",colSums(v),a,(a-cf)/(1-cf),(a-cg)/(1-cg),"\n")
stopifnot(all(rowSums(v)==3),abs((a-cg)/(1-cg)-.649567619)<1e-9)
