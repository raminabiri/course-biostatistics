d <- read.csv("data/M41_practice.csv")
rx <- residuals(lm(marker_x~age,d))
ry <- residuals(lm(marker_y~age,d))
r <- cor(rx,ry)
semi <- cor(rx,d$marker_y)
df <- nrow(d)-3
t <- r*sqrt(df/(1-r^2))
delta <- summary(lm(marker_y~age+marker_x,d))$r.squared-summary(lm(marker_y~age,d))$r.squared
cat(cor(d$marker_x,d$marker_y),r,semi,delta,2*pt(-abs(t),df),"\n")
stopifnot(abs(semi^2-delta)<1e-12)
