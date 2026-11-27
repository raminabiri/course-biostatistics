* Run from the M33 folder or change the two occurrences of the CSV path.
GET DATA /TYPE=TXT /FILE='data/practice.csv'
 /DELCASE=LINE /DELIMITERS=',' /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=a F1.0 b F1.0 replicate F2.0 baseline F8.2 value F10.2.

* Transform the response separately for each effect and rank over all rows.
COMPUTE all_rows=1.
IF a=0 a0=value.
IF a=1 a1=value.
IF b=0 b0=value.
IF b=1 b1=value.
IF a=0 AND b=0 cell00=value.
IF a=0 AND b=1 cell01=value.
IF a=1 AND b=0 cell10=value.
IF a=1 AND b=1 cell11=value.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES /BREAK=all_rows
 /mean_all=MEAN(value)
 /mean_a0=MEAN(a0) /mean_a1=MEAN(a1)
 /mean_b0=MEAN(b0) /mean_b1=MEAN(b1)
 /mean_00=MEAN(cell00) /mean_01=MEAN(cell01)
 /mean_10=MEAN(cell10) /mean_11=MEAN(cell11).
COMPUTE mean_a=(1-a)*mean_a0+a*mean_a1.
COMPUTE mean_b=(1-b)*mean_b0+b*mean_b1.
COMPUTE mean_cell=(1-a)*(1-b)*mean_00+(1-a)*b*mean_01+a*(1-b)*mean_10+a*b*mean_11.
COMPUTE al_a=RND((value-mean_cell+mean_a-mean_all)*1000000)/1000000.
COMPUTE al_b=RND((value-mean_cell+mean_b-mean_all)*1000000)/1000000.
COMPUTE al_ab=RND((value-mean_a-mean_b+mean_all)*1000000)/1000000.
RANK VARIABLES=al_a /RANK INTO r_a /TIES=MEAN.
RANK VARIABLES=al_b /RANK INTO r_b /TIES=MEAN.
RANK VARIABLES=al_ab /RANK INTO r_ab /TIES=MEAN.
RANK VARIABLES=value /RANK INTO r_y /TIES=MEAN.

* Orthogonal contrasts for the balanced 2 by 2 independent design.
COMPUTE sign_a=2*a-1.
COMPUTE sign_b=2*b-1.
COMPUTE sign_ab=sign_a*sign_b.
COMPUTE cross_a_a=r_a*sign_a.
COMPUTE cross_a_b=r_a*sign_b.
COMPUTE cross_a_ab=r_a*sign_ab.
COMPUTE cross_b_a=r_b*sign_a.
COMPUTE cross_b_b=r_b*sign_b.
COMPUTE cross_b_ab=r_b*sign_ab.
COMPUTE cross_ab_a=r_ab*sign_a.
COMPUTE cross_ab_b=r_ab*sign_b.
COMPUTE cross_ab_ab=r_ab*sign_ab.
COMPUTE cross_y_a=r_y*sign_a.
COMPUTE cross_y_b=r_y*sign_b.
COMPUTE cross_y_ab=r_y*sign_ab.

AGGREGATE /OUTFILE=* /BREAK=all_rows
 /n_obs=N
 /sum_a_a=SUM(cross_a_a)
 /sum_a_b=SUM(cross_a_b)
 /sum_a_ab=SUM(cross_a_ab)
 /sd_a=SD(r_a)
 /sum_b_a=SUM(cross_b_a)
 /sum_b_b=SUM(cross_b_b)
 /sum_b_ab=SUM(cross_b_ab)
 /sd_b=SD(r_b)
 /sum_ab_a=SUM(cross_ab_a)
 /sum_ab_b=SUM(cross_ab_b)
 /sum_ab_ab=SUM(cross_ab_ab)
 /sd_ab=SD(r_ab)
 /sum_y_a=SUM(cross_y_a)
 /sum_y_b=SUM(cross_y_b)
 /sum_y_ab=SUM(cross_y_ab)
 /sd_y=SD(r_y).

COMPUTE ss_a_a=sum_a_a**2/n_obs.
COMPUTE ss_a_b=sum_a_b**2/n_obs.
COMPUTE ss_a_ab=sum_a_ab**2/n_obs.
COMPUTE total_a=sd_a**2*(n_obs-1).
COMPUTE mse_a=(total_a-ss_a_a-ss_a_b-ss_a_ab)/(n_obs-4).
COMPUTE f_a=ss_a_a/mse_a.
COMPUTE p_a=1-CDF.F(f_a,1,n_obs-4).
COMPUTE ss_b_a=sum_b_a**2/n_obs.
COMPUTE ss_b_b=sum_b_b**2/n_obs.
COMPUTE ss_b_ab=sum_b_ab**2/n_obs.
COMPUTE total_b=sd_b**2*(n_obs-1).
COMPUTE mse_b=(total_b-ss_b_a-ss_b_b-ss_b_ab)/(n_obs-4).
COMPUTE f_b=ss_b_b/mse_b.
COMPUTE p_b=1-CDF.F(f_b,1,n_obs-4).
COMPUTE ss_ab_a=sum_ab_a**2/n_obs.
COMPUTE ss_ab_b=sum_ab_b**2/n_obs.
COMPUTE ss_ab_ab=sum_ab_ab**2/n_obs.
COMPUTE total_ab=sd_ab**2*(n_obs-1).
COMPUTE mse_ab=(total_ab-ss_ab_a-ss_ab_b-ss_ab_ab)/(n_obs-4).
COMPUTE f_ab=ss_ab_ab/mse_ab.
COMPUTE p_ab=1-CDF.F(f_ab,1,n_obs-4).
COMPUTE ss_y_a=sum_y_a**2/n_obs.
COMPUTE ss_y_b=sum_y_b**2/n_obs.
COMPUTE ss_y_ab=sum_y_ab**2/n_obs.
COMPUTE total_y=sd_y**2*(n_obs-1).
COMPUTE h_a=ss_y_a/(total_y/(n_obs-1)).
COMPUTE ph_a=1-CDF.CHISQ(h_a,1).
COMPUTE h_b=ss_y_b/(total_y/(n_obs-1)).
COMPUTE ph_b=1-CDF.CHISQ(h_b,1).
COMPUTE h_ab=ss_y_ab/(total_y/(n_obs-1)).
COMPUTE ph_ab=1-CDF.CHISQ(h_ab,1).
FORMATS f_a f_b f_ab h_a h_b h_ab (F10.5)
 p_a p_b p_ab ph_a ph_b ph_ab (E12.5).
LIST f_a p_a f_b p_b f_ab p_ab.
LIST h_a ph_a h_b ph_b h_ab ph_ab.

* Rank ANCOVA via pooled rank regression at level b=0.
GET DATA /TYPE=TXT /FILE='data/practice.csv'
 /DELCASE=LINE /DELIMITERS=',' /ARRANGEMENT=DELIMITED /FIRSTCASE=2
 /VARIABLES=a F1.0 b F1.0 replicate F2.0 baseline F8.2 value F10.2.
SELECT IF b=0.
EXECUTE.
RANK VARIABLES=baseline value /RANK INTO r_base r_resp /TIES=MEAN.
COMPUTE all_rows=1.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES /BREAK=all_rows
 /mean_base=MEAN(r_base) /mean_resp=MEAN(r_resp).
COMPUTE cross_product=(r_base-mean_base)*(r_resp-mean_resp).
COMPUTE square_base=(r_base-mean_base)**2.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES /BREAK=all_rows
 /sxy=SUM(cross_product) /sxx=SUM(square_base).
COMPUTE slope=sxy/sxx.
COMPUTE rank_resid=r_resp-mean_resp-slope*(r_base-mean_base).
TITLE "Quade-style rank ANCOVA".
ONEWAY rank_resid BY a.
