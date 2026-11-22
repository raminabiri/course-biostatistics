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
group <- unique(d[c("id","group")])$group
change <- x[,3]-x[,1]
cat("L1:",rm(z-x),"\n")
cat("L2:",t.test(change[group==1],change[group==0],var.equal=TRUE)$statistic,
    t.test(change[group==1],change[group==0],var.equal=TRUE)$p.value,"\n")
cat("L3:",rm(x,group),"\n")
