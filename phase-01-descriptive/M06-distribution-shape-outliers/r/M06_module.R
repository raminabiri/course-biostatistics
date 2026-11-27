x <- read.csv("data/M06_module.csv")$wait
q <- as.numeric(quantile(x,c(.25,.5,.75),type=7))
width <- q[3]-q[1]
bounds <- c(q[1]-1.5*width,q[3]+1.5*width)
flagged <- x[x<bounds[1] | x>bounds[2]]
stopifnot(identical(q,c(3,5,7)),identical(bounds,c(-3,13)),identical(flagged,40L))
print(c(q1=q[1],median=q[2],q3=q[3],IQR=width,lower=bounds[1],upper=bounds[2],log_diff=log2(40/8)))
