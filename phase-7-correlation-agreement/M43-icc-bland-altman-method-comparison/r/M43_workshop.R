d <- read.csv("data/M43_methods.csv")
a <- d$method_a; b <- d$method_b
x <- cbind(a,b); n <- nrow(x); k <- ncol(x)
g <- mean(x); mi <- rowMeans(x); mr <- colMeans(x)
msi <- k*sum((mi-g)^2)/(n-1)
msr <- n*sum((mr-g)^2)/(k-1)
within <- sweep(x,1,mi)
mse <- sum((sweep(within,2,mr)+g)^2)/((n-1)*(k-1))
msw <- sum(within^2)/(n*(k-1))
icc <- c((msi-msw)/(msi+(k-1)*msw),
         (msi-mse)/(msi+(k-1)*mse+k*(msr-mse)/n),
         (msi-mse)/(msi+(k-1)*mse),
         (msi-mse)/(msi+(msr-mse)/n))
cat("L1:",msi,msr,mse,msw,icc,"\n")
diff <- b-a
cov_n <- cov(a,b)*(n-1)/n
vars <- c(var(a),var(b))*(n-1)/n
ccc <- 2*cov_n/(sum(vars)+(mean(a)-mean(b))^2)
cat("L2:",mean(diff),sd(diff),mean(diff)+c(-1,1)*1.96*sd(diff),ccc,"\n")
delta <- vars[2]-vars[1]
deming <- (delta+sqrt(delta^2+4*cov_n^2))/(2*cov_n)
pairs <- combn(seq_along(a),2)
slopes <- (b[pairs[2,]]-b[pairs[1,]])/(a[pairs[2,]]-a[pairs[1,]])
stopifnot(all(is.finite(slopes) & slopes> -1))
pb <- median(slopes)
cat("L3:",deming,mean(b)-deming*mean(a),pb,median(b-pb*a),"\n")
stopifnot(n==24, abs(icc[2]-.9585648192)<1e-9, abs(pb-1.06)<1e-12)
