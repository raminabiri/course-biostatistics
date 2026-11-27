d<-read.csv("data/M80_L2.csv")
p<-with(d,t1/(t1+t2))
score<-function(i){
 g<-seq_along(p) %in% i
 w<-sum((p-ave(p,g))^2)
 (sum((p-mean(p))^2)-w)/(w/4)
}
observed<-score(which(d$group=="A"))
null<-combn(6,3,score)
prob<-mean(null>=observed-1e-10)
stopifnot(abs(observed-54)<1e-10,prob==.1)
print(c(F=observed,p=prob))
if(requireNamespace("vegan",quietly=TRUE)){
 dist<-vegan::vegdist(d[c("t1","t2")],method="bray")
 fit<-vegan::adonis2(dist~group,data=d,permutations=0)
 print(fit[, c("Df", "SumOfSqs", "R2", "F")])
 stopifnot(abs(fit$F[1]-54)<1e-10)
}
