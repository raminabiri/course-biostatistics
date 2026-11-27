d <- read.csv("data/M44_scale.csv")
raw <- as.matrix(d[,2:6]); x <- raw
x[,4] <- 6 - x[,4]
alpha <- function(x) {
  k <- ncol(x)
  k/(k-1)*(1-sum(apply(x,2,var))/var(rowSums(x)))
}
total <- rowSums(x)
item_total <- sapply(1:5,function(j) cor(x[,j],total-x[,j]))
cat("L1:",alpha(raw),alpha(x),item_total,"\n")
fit <- factanal(x,1)
l <- as.numeric(fit$loadings)
omega <- sum(l)^2/(sum(l)^2+sum(fit$uniquenesses))
cat("L2:",l,omega,cor(total,d$total_retest),"\n")
x <- as.matrix(read.csv("data/M44_rasch.csv")[,-1])
k <- ncol(x)
patterns <- as.matrix(expand.grid(rep(list(0:1),k)))
pattern_scores <- rowSums(patterns)
counts <- tabulate(rowSums(x)+1,nbins=k+1)
difficulties <- function(free) c(free,-sum(free))
logsumexp <- function(x) { anchor <- max(x); anchor + log(sum(exp(x-anchor))) }
loss <- function(free) {
  delta <- difficulties(free)
  norm <- sapply(0:k,function(s) logsumexp(-drop(patterns[pattern_scores==s,,drop=FALSE] %*% delta)))
  sum(colSums(x)*delta)+sum(counts*norm)
}
fit <- optim(rep(0,k-1),loss,method="BFGS",control=list(reltol=1e-12))
d <- difficulties(fit$par)
theta3 <- uniroot(function(th) sum(plogis(th-d))-3,c(-15,15),tol=1e-10)$root
cat("L3:",colSums(x),counts,d,theta3,plogis(theta3-d),"\n")
stopifnot(abs(omega-.83618)<.0001,fit$convergence==0,abs(sum(d))<1e-12)
