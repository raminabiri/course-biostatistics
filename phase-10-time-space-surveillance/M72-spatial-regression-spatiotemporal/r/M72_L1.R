d <- read.csv("data/M72_L1.csv")
w <- matrix(c(0,1,0,.5,0,.5,0,1,0),3,byrow=TRUE)
spatial <- solve(diag(3)-.5*w,c(1,2,3))
smooth <- Reduce(function(last,y) .25*y+.75*last,d$requests,init=10,accumulate=TRUE)[-1]
stopifnot(max(abs(spatial-c(3,4,5)))<1e-12, which(smooth>13)==4)
print(spatial)
print(smooth)
