d <- read.csv("data/M73_L2.csv")
area <- sum(diff(d$hour)*(head(d$conc,-1)+tail(d$conc,-1))/2)
end <- subset(d,hour>=2 & conc>0)
half_life <- -log(2)/coef(lm(log(conc)~hour,end))[2]
peak <- which.max(d$conc)
stopifnot(area==14.5,abs(half_life-1)<1e-12,peak==2)
print(c(AUC=area,Cmax=d$conc[peak],Tmax=d$hour[peak],half_life=unname(half_life)))
