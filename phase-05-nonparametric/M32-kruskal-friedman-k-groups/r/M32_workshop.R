d <- read.csv("data/practice.csv")
a <- subset(d,design=="independent")
b <- subset(d,design=="blocked")
ranks <- rank(a$value); group <- a$group
n <- as.numeric(table(group)); N <- length(ranks)
means <- as.numeric(tapply(ranks,group,mean))
kw <- kruskal.test(a$value,factor(group))
cat("L1:",kw$statistic,kw$p.value,"\n")
pairs <- combn(1:3,2)
ss_within <- sum((ranks-means[group])^2)
pdunn <- apply(pairs,2,function(p) 2*pnorm(-abs(diff(means[p]))/sqrt(var(ranks)*sum(1/n[p]))))
pcon <- apply(pairs,2,function(p) 2*pt(-abs(diff(means[p]))/sqrt(ss_within/(N-3)*sum(1/n[p])),N-3))
cat("Dunn Holm:",p.adjust(pdunn,"holm"),"Conover Holm:",p.adjust(pcon,"holm"),"\n")
values <- split(a$value,group)
J <- sum(apply(pairs,2,function(p) sum(outer(values[[p[1]]],values[[p[2]]],"<")) + 0.5*sum(outer(values[[p[1]]],values[[p[2]]],"=="))))
mu <- (N^2-sum(n^2))/4
v <- (N*(N-1)*(2*N+5)-sum(n*(n-1)*(2*n+5)))/72
if (anyDuplicated(a$value)) {
  cat("L2:", J, "Skip normal p with ties\n")
} else {
  cat("L2:", J, pnorm((J-mu)/sqrt(v),lower.tail=FALSE),"\n")
}
stopifnot(all(table(b$block, b$group) == 1))
mat <- as.matrix(xtabs(value~block+group,b))
fr <- friedman.test(mat); qu <- quade.test(mat)
cat("L3:",fr$statistic,fr$p.value,fr$statistic/(nrow(mat)*(ncol(mat)-1)),qu$statistic,qu$p.value,"\n")
rank_matrix <- t(apply(mat,1,rank))
nb <- nrow(mat)
k <- ncol(mat)
rank_mean <- colMeans(rank_matrix)
d <- abs(apply(pairs,2,function(pair) diff(rank_mean[pair])))
pn <- ptukey(d/sqrt(k*(k+1)/(12*nb)),k,Inf,lower.tail=FALSE)
residual <- sweep(rank_matrix,2,rank_mean)
df <- (nb-1)*(k-1)
ms <- sum(residual^2)/df
pc <- 2*pt(-d/sqrt(2*ms/nb),df)
cat("L3 Nemenyi:",pn,"blocked Conover Holm:",p.adjust(pc,"holm"),"\n")

# Exact tail for three conditions without within-block ties.
if (all(apply(rank_matrix, 1, function(row) all(sort(row) == 1:3)))) {
  orders <- expand.grid(first=1:3, second=1:3)
  orders <- subset(orders, first != second)
  size <- 3*nb+1L
  counts <- matrix(0, size, size)
  counts[1, 1] <- 1
  for (block in seq_len(nb)) {
    updated <- matrix(0, size, size)
    states <- which(counts > 0, arr.ind=TRUE)
    for (i in seq_len(nrow(states))) {
      x <- states[i, 1]
      y <- states[i, 2]
      for (j in seq_len(nrow(orders))) {
        a <- x + orders$first[j]
        b <- y + orders$second[j]
        updated[a, b] <- updated[a, b] + counts[x, y]
      }
    }
    counts <- updated
  }
  observed <- sum(colSums(rank_matrix)^2)
  at_least_observed <- outer(0:(size-1), 0:(size-1),
                            function(x,y) x^2+y^2+(6*nb-x-y)^2) >= observed
  tail <- sum(counts[at_least_observed])
  cat("Friedman exact:", tail, "/", sum(counts), "=", tail/sum(counts), "\n")
}
