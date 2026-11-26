d <- read.csv("data/M41_practice.csv")
x <- d$marker_x; y <- d$marker_y
binary <- table(x>=55,y>=65)
ordinal <- table(cut(x,c(-Inf,45,65,Inf),right=FALSE),
                 cut(y,c(-Inf,55,75,Inf),right=FALSE))
estimate <- function(tab) {
  edges <- function(margin) c(-Inf,qnorm(head(cumsum(margin)/sum(margin),-1)),Inf)
  a <- edges(rowSums(tab)); b <- edges(colSums(tab))
  loss <- function(rho) {
    sd <- sqrt(1-rho^2)
    value <- 0
    for (i in seq_len(nrow(tab))) for (j in seq_len(ncol(tab))) {
      if (tab[i,j]==0) next
      probability <- integrate(function(t) dnorm(t)*
         (pnorm((b[j+1]-rho*t)/sd)-pnorm((b[j]-rho*t)/sd)),
          a[i],a[i+1],rel.tol=1e-9)$value
      value <- value - tab[i,j]*log(probability)
    }
    value
  }
  optimize(loss,c(-.98,.98),tol=1e-8)$minimum
}
out <- c(tetrachoric=estimate(binary),polychoric=estimate(ordinal))
print(out)
stopifnot(max(abs(out-c(.827761,.892447)))<1e-5)
