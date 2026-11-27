d <- read.csv("data/M60_table.csv")
cell <- function(a,b) with(d,sum(count[reference==a & test==b]))
tp <- cell(1,1); fn <- cell(1,0); fp <- cell(0,1); tn <- cell(0,0)
se <- tp/(tp+fn); sp <- tn/(tn+fp)
out <- c(sensitivity=se,specificity=sp,PPV=tp/(tp+fp),NPV=tn/(tn+fn),
         LRplus=se/(1-sp),LRminus=(1-se)/sp)
print(out)
stopifnot(max(abs(out-c(.9,.8,.75,12/13,4.5,.125)))<1e-10)
