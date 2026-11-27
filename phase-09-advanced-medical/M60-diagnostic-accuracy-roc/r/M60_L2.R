d <- read.csv("data/M60_roc.csv")
place <- function(x) {
  a <- outer(x[d$reference==1],x[d$reference==0],"-")
  h <- (a>0)+.5*(a==0)
  list(p=rowMeans(h),n=colMeans(h),auc=mean(h))
}
a <- place(d$score_a); b <- place(d$score_b)
v <- var(b$p-a$p)/length(a$p)+var(b$n-a$n)/length(a$n)
z <- (b$auc-a$auc)/sqrt(v)
print(c(A=a$auc,B=b$auc,variance=v,z=z,p=2*pnorm(-abs(z))))
stopifnot(abs(v-.0048)<1e-10)
