d <- read.csv("data/M71_L1.csv")
sir <- d$observed/d$expected
z <- sir-mean(sir)
w <- 1*(abs(outer(d$x,d$x,"-"))==1)
i <- nrow(d)/sum(w)*as.numeric(t(z)%*%w%*%z)/sum(z^2)
smooth <- (d$observed+5)/(d$expected+5)
stopifnot(abs(i-.4)<1e-12,abs(smooth[4]-5/3)<1e-12)
print(data.frame(area=d$area,sir,smooth))
print(i)
