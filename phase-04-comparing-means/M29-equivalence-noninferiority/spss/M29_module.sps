GET DATA /TYPE=TXT /FILE='data/means.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=id F4.0 group_id F1.0 value F16.8.
COMPUTE new_value=$SYSMIS.
COMPUTE ref_value=$SYSMIS.
IF group_id=1 new_value=value.
IF group_id=0 ref_value=value.
AGGREGATE /OUTFILE=*
 /n_new=N(new_value) /n_ref=N(ref_value) /m_new=MEAN(new_value) /m_ref=MEAN(ref_value) /s_new=SD(new_value) /s_ref=SD(ref_value).
COMPUTE d=m_new-m_ref.
COMPUTE df=n_new+n_ref-2.
COMPUTE pooled=((n_new-1)*s_new**2+(n_ref-1)*s_ref**2)/df.
COMPUTE se=SQRT(pooled*(1/n_new+1/n_ref)).
COMPUTE p_lower=1-CDF.T((d+2)/se,df).
COMPUTE p_upper=CDF.T((d-2)/se,df).
COMPUTE half=IDF.T(.95,df)*se.
COMPUTE ci_lo=d-half.
COMPUTE ci_hi=d+half.
COMPUTE p_tost=MAX(p_lower,p_upper).
FORMATS m_new m_ref d se p_lower p_upper p_tost ci_lo ci_hi (F13.9).
LIST VARIABLES=n_new n_ref m_new m_ref d se p_lower p_upper p_tost ci_lo ci_hi.
GET DATA /TYPE=TXT /FILE='data/proportions.csv' /DELCASE=LINE /DELIMITERS=","
 /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES=id F4.0 group_id F1.0 response F16.8.
COMPUTE new_value=$SYSMIS.
COMPUTE ref_value=$SYSMIS.
IF group_id=1 new_value=response.
IF group_id=0 ref_value=response.
AGGREGATE /OUTFILE=*
 /n_new=N(new_value) /n_ref=N(ref_value) /m_new=MEAN(new_value) /m_ref=MEAN(ref_value).
COMPUTE d=m_new-m_ref.
COMPUTE se=SQRT(m_new*(1-m_new)/n_new+m_ref*(1-m_ref)/n_ref).
COMPUTE p_lower=1-CDF.NORMAL((d+.12)/se,0,1).
COMPUTE p_upper=CDF.NORMAL((d-.12)/se,0,1).
COMPUTE half=IDF.NORMAL(.95,0,1)*se.
COMPUTE ci_lo=d-half.
COMPUTE ci_hi=d+half.
COMPUTE p_tost=MAX(p_lower,p_upper).
FORMATS m_new m_ref d se p_lower p_upper p_tost ci_lo ci_hi (F13.9).
LIST VARIABLES=n_new n_ref m_new m_ref d se p_lower p_upper p_tost ci_lo ci_hi.
