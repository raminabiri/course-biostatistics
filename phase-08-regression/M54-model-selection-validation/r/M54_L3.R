d <- read.csv("data/M54_penalty.csv")
lambda <- c(0,5,10,20)
xx <- sum(d$x^2)
xy <- sum(d$x*d$y)
ridge <- xy/(xx+lambda)
lasso <- sign(xy)*pmax(abs(xy)-lambda,0)/xx
print(data.frame(lambda,ridge,lasso))
stopifnot(tail(lasso,1)==0,abs(tail(ridge,1)-2/3)<1e-12)
