d <- read.csv("data/practice.csv")
make_matrix <- function(level) {
  as.matrix(xtabs(value~id+time,subset(d,d$condition==level)))
}
x <- make_matrix(0)
z <- make_matrix(1)
rm <- function(y, g=rep(0,nrow(y))) {
  n <- nrow(y); k <- ncol(y)
  yt <- y-rowMeans(y)
  means <- unique(g)
  group_rows <- do.call(rbind,lapply(means,function(i) colMeans(yt[g==i,,drop=FALSE])))
  weights <- as.numeric(table(g))
  ss_error <- sum((yt-group_rows[match(g,means),])^2)
  center <- colMeans(yt)
  ss <- if(length(means)==1) n*sum(center^2) else sum(weights*rowSums(sweep(group_rows,2,center)^2))
  df1 <- (k-1)*max(1,length(means)-1); df2 <- (n-length(means))*(k-1)
  value <- (ss/df1)/(ss_error/df2)
  c(F=value,p=pf(value,df1,df2,lower.tail=FALSE))
}
cat("L1:",rm(x),"\n")
c <- cbind(c(1,-1,0)/sqrt(2),c(1,1,-2)/sqrt(6))
s <- cov(x%*%c); e <- sum(diag(s))^2/(2*sum(s*s))
cat("L2 epsilon:",e," adjusted P:",pf(rm(x)[1],2*e,22*e,lower.tail=FALSE),"\n")
cat("L3:",mean(x[,3]-x[,1]),t.test(x[,3],x[,1],paired=TRUE)$p.value,"\n")
