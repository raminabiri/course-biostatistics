# Run with Rscript from any working directory; base R only.
args <- commandArgs(trailingOnly=FALSE)
script <- sub('^--file=', '', args[grepl('^--file=', args)])
if (length(script) != 1) stop('Run this file with Rscript.')
data_dir <- file.path(dirname(normalizePath(script)), '..', 'data')
p <- read.csv(file.path(data_dir, 'M01_bank_patients.csv'))
f <- read.csv(file.path(data_dir, 'M01_bank_followup.csv'))
l <- read.csv(file.path(data_dir, 'M01_bank_laboratory.csv'))
stopifnot(nrow(p)==1000, !anyNA(p$patient_id), !anyDuplicated(p$patient_id),
          nrow(f)==3000, !anyDuplicated(f[c('patient_id','day')]),
          all(table(f$patient_id)==3), setequal(f$day,c(0,3,7)),
          all(f$patient_id %in% p$patient_id), sum(is.na(p$crp))==50,
          sum(is.na(f$crp))==150, sum(is.na(f$crp[f$day==7]))==100,
          all((f$status=='not_collected') == is.na(f$crp)),
          nrow(l)==200, length(unique(l$sample_id))==100,
          !anyDuplicated(l[c('sample_id','replicate')]), all(table(l$sample_id)==2))
b <- f[f$day==0, ]; b <- b[match(p$patient_id,b$patient_id), ]
stopifnot(isTRUE(all.equal(p$crp,b$crp)))
cat('PASS: 1000 patients; 3000 visits; 100 samples / 200 readings; 50 baseline gaps; 100 day-7 gaps; 150 visit gaps.\n')
