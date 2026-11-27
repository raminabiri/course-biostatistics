d<-read.csv("data/P02.csv")
t<-aggregate(cbind(event,time)~exposure,d,sum)
rate<-t$event/t$time
stopifnot(all(t$time==c(40,30)),abs(rate[2]/rate[1]-20/9)<1e-12)
print(t)
print(c(rates=100*rate,rate_ratio=rate[2]/rate[1]))
