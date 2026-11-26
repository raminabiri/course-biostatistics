d <- read.csv("data/M41_practice.csv")
x <- d$marker_x; y <- d$marker_y
h <- x>=55; k <- y>=65
p <- mean(h)
pb <- cor(h,y)
xb <- cut(x,c(-Inf,45,65,Inf),right=FALSE)
yb <- cut(y,c(-Inf,55,75,Inf),right=FALSE)
tab <- table(xb,yb)
x2 <- unname(chisq.test(tab)$statistic)
n <- nrow(d)
eta <- sqrt(sum(table(xb)*(tapply(y,xb,mean)-mean(y))^2)/sum((y-mean(y))^2))
print(table(h,k))
print(tab)
out <- c(pb=pb,biserial=pb*sqrt(p*(1-p))/dnorm(qnorm(1-p)),
         phi=cor(h,k), V=sqrt(x2/(2*n)), C=sqrt(x2/(n+x2)),eta=eta)
print(out)
stopifnot(abs(out["eta"]-.7676913121)<1e-9)
