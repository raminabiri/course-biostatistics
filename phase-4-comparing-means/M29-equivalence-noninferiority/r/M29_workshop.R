tost <- function(d,se,lower,upper,dist,qdist) {
  h <- qdist(.95)*se
  p <- c(1-dist((d-lower)/se),dist((d-upper)/se))
  c(p, max(p), d-h,d+h)
}
cat("L1:",all(c(-1.1,1.3)>-2 & c(-1.1,1.3)<2),"\n")
cat("L2:",tost(.4,.6,-2,2,function(x)pt(x,38),function(x)qt(x,38)),"\n")
se <- sqrt(.45*.55/200+.42*.58/200)
cat("L3:",tost(.45-.42,se,-.12,.12,pnorm,qnorm),"\n")
