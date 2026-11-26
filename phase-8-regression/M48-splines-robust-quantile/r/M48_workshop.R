d <- read.csv("data/M48_practice.csv")
x <- d$x; y <- d$y
basis <- function(x) (pmax(x-4,0)^3-2*pmax(x-12,0)^3+pmax(x-20,0)^3)/256
m <- lm(y~x)
rss <- sapply(list(m,lm(y~x+I(x^2)),lm(y~x+basis(x))),deviance)
cat("L1:",rss,"\n")
loss <- function(b) {
  u <- abs((y-b[1]-b[2]*x)/2)
  sum(ifelse(u<=1.345,u^2/2,1.345*(u-1.345/2)))
}
robust <- optim(coef(m),loss,method="BFGS",control=list(reltol=1e-12))
cat("L2:",coef(m),robust$par,"\n")
pairs <- combn(seq_along(x),2)
stopifnot(!anyDuplicated(x))
slope <- (y[pairs[2,]]-y[pairs[1,]])/(x[pairs[2,]]-x[pairs[1,]])
intercept <- y[pairs[1,]]-slope*x[pairs[1,]]
for (tau in c(.5,.9)) {
  objectives <- sapply(seq_along(slope),function(j) {
    r <- y-intercept[j]-slope[j]*x
    sum(ifelse(r>=0,tau*r,(tau-1)*r))
  })
  best <- which.min(objectives)
  cat("L3:",tau,intercept[best],slope[best],objectives[best],"\n")
}
stopifnot(robust$convergence==0,abs(rss[3]-216.6125)<1e-4)
