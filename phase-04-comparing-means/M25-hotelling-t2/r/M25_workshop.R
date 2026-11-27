d <- read.csv("data/practice.csv")
y <- as.matrix(d[c("y","z")])
ht <- function(d, s, weight, denom, df2) {
  p <- length(d)
  tt <- weight*drop(crossprod(d,solve(s,d)))
  ff <- tt*df2/(p*denom)
  c(T2=tt,F=ff,p=pf(ff,p,df2,lower.tail=FALSE))
}
one <- function(y,mu) ht(colMeans(y)-mu,cov(y),nrow(y),nrow(y)-1,nrow(y)-ncol(y))
a <- y[d$a==0,]; b <- y[d$a==1,]
cat("L1:",one(a,c(47,27)),"\n")
cat("L2:",ht(colMeans(b)-colMeans(a),(cov(a)+cov(b))/2,8,30,29),"\n")
cat("L3:",one(y-as.matrix(d[c("y0","z0")]),c(0,0)),"\n")
