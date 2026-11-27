ks_permutation <- function(a,b) {
  n1 <- length(a)
  n2 <- length(b)
  levels <- sort(unique(c(a,b)))
  cnt1 <- tabulate(match(a,levels),nbins=length(levels))
  cnt2 <- tabulate(match(b,levels),nbins=length(levels))
  gap <- max(abs(cumsum(cnt1)*n2-cumsum(cnt2)*n1))
  if (gap==0) return(c(D=0,p=1))
  paths <- c(1,rep(0,n1))
  total <- 0
  for (m in cnt1+cnt2) {
    next_paths <- rep(0,n1+1)
    for (i in which(paths > 0)-1) {
      for (k in 0:m) {
        j <- i+k
        used_b <- total+m-j
        if (j<=n1 && used_b<=n2 && abs(j*n2-used_b*n1)<gap) {
          next_paths[j+1] <- next_paths[j+1]+paths[i+1]*choose(m,k)
        }
      }
    }
    paths <- next_paths
    total <- total+m
  }
  c(D=gap/(n1*n2),p=1-paths[n1+1]/choose(n1+n2,n1))
}
report <- function(file, exact) {
  d <- read.csv(file)
  a <- d$value[d$group=="A"]
  b <- d$value[d$group=="B"]
  w <- wilcox.test(a,b,exact=exact,correct=FALSE)
  reference <- ks_permutation(a,b)
  tab <- table(d$group,d$value>median(d$value))
  cat(file, "\nL1: U of A and P:", w$statistic,w$p.value,"\n")
  cat("L2: conditional KS:"); print(reference)
  cat("L3: HL, median table and Fisher P:\n")
  print(median(outer(a,b,"-")))
  print(tab)
  print(fisher.test(tab)$p.value)
}
report("data/practice.csv",TRUE)
report("data/extended.csv",FALSE)
