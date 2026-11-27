frame <- read.csv("data/M03_frame.csv")
trial <- head(read.csv("data/M03_trial.csv"),4)
sample_rows <- head(frame[order(frame$u,frame$id),], 10)
trial <- trial[order(trial$u,trial$id),]
trial$arm <- rep(c("program","control"),each=2)
stopifnot(nrow(frame)==600, sum(frame$htn)==165, sum(sample_rows$htn)==4,
          identical(sample_rows$id,c(552L,542L,273L,104L,361L,229L,279L,440L,127L,175L)),
          identical(trial$id,c(3L,2L,1L,4L)))
print(c(frame=mean(frame$htn), sampled=mean(sample_rows$htn), points=100*(mean(sample_rows$htn)-mean(frame$htn))))
print(trial)
