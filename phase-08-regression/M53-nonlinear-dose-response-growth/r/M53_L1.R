d <- read.csv("data/M53_curve.csv")
curve <- function(x,low,high,mid,slope,shape=1) {
  low+(high-low)/(1+(mid/x)^slope)^shape
}
start <- c(low=10,high=90,mid=2,slope=1.5)
initial <- do.call(curve,c(list(x=d$input),as.list(start)))
fit <- nls(observed~curve(input,low,high,mid,slope),data=d,start=as.list(start))
print(coef(fit))
print(c(initial_error=sum((d$observed-initial)^2),fitted_error=deviance(fit)))
stopifnot(curve(2,10,90,2,1.5)==50,curve(2,10,90,2,1.5,2)==30)
