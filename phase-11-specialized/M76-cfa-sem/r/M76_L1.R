d<-read.csv("data/M76_L1.csv")
pred <- with(d,loading_i*loading_j)
res <- d$observed-pred
stopifnot(max(abs(res-c(.04,0,-.02)))<1e-10)
print(data.frame(pred,res))
