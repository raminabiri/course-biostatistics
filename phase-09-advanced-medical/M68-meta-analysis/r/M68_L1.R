d <- read.csv("data/M68_L1.csv")
w <- 1/d$se^2
pooled <- weighted.mean(d$effect,w)
q <- sum(w*(d$effect-pooled)^2)
df <- nrow(d)-1
tau2 <- max(0,(q-df)/(sum(w)-sum(w^2)/sum(w)))
wr <- 1/(d$se^2+tau2)
stopifnot(pooled==3,q==14,tau2==6)
print(c(common=pooled,Q=q,I2=(q-df)/q,tau2=tau2,random=weighted.mean(d$effect,wr),SE=sqrt(1/sum(wr))))
