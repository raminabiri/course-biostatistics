d <- read.csv("data/M75_L1.csv")
pca <- prcomp(d[c("fatigue","activity")], scale.=TRUE)
eigenvalues <- pca$sdev^2
stopifnot(abs(eigenvalues[1]-(1+1/sqrt(2)))<1e-12)
print(eigenvalues)
print(eigenvalues/sum(eigenvalues))
print(pca$x)
