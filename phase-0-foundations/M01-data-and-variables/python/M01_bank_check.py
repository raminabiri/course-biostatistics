"""Check the synthetic teaching bank; run from any working directory."""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / 'data'
p = pd.read_csv(DATA / 'M01_bank_patients.csv')
f = pd.read_csv(DATA / 'M01_bank_followup.csv')
l = pd.read_csv(DATA / 'M01_bank_laboratory.csv')
assert len(p) == 1000 and p.patient_id.is_unique
assert not p.patient_id.isna().any()
assert len(f) == 3000 and not f.duplicated(['patient_id', 'day']).any()
assert f.groupby('patient_id').size().eq(3).all()
assert set(f.day) == {0, 3, 7}
assert f.patient_id.isin(p.patient_id).all()
assert p.crp.isna().sum() == 50
assert f.crp.isna().sum() == 150
assert f.loc[f.day.eq(7), 'crp'].isna().sum() == 100
assert f.status.eq('not_collected').equals(f.crp.isna())
assert len(l) == 200 and l.sample_id.nunique() == 100
assert not l.duplicated(['sample_id', 'replicate']).any()
assert l.groupby('sample_id').size().eq(2).all()
baseline = f.loc[f.day.eq(0)].set_index('patient_id').crp.sort_index()
pd.testing.assert_series_equal(p.set_index('patient_id').crp.sort_index(), baseline)
for name, frame in [('patients', p), ('followup', f), ('laboratory', l)]:
    excel = pd.read_excel(DATA / 'M01_training_bank.xlsx', sheet_name=name)
    pd.testing.assert_frame_equal(frame, excel)
print('PASS: 1000 patients; 3000 visits; 100 samples / 200 readings; 50 baseline gaps; 100 day-7 gaps; 150 visit gaps; Excel = CSV.')
