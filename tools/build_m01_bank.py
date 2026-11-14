"""Rebuild synthetic M01 workbooks and CSV files. No real patient data."""
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'phase-0-foundations/M01-data-and-variables/data'

def build():
    patients = []
    followup = []
    laboratory = []
    for i in range(1, 1001):
        patients.append([i, 18 + i % 73, 1 + i % 2, 1 + i % 3,
                         1 + (i // 7) % 3, None if i % 20 == 0 else 5 + (i * 7) % 96])
        baseline = 5 + (i * 7) % 96
        for day, factor in [(0, 1), (3, .7), (7, .4)]:
            missing = (day == 7 and i % 10 == 0) or (day == 0 and i % 20 == 0)
            followup.append([i, day, None if missing else round(baseline * factor, 1),
                             'not_collected' if missing else 'recorded'])
    for sample in range(1, 101):
        for replicate, delta in [(1, -.2), (2, .2)]:
            laboratory.append([sample, 1 + sample % 2, replicate,
                               round(20 + sample % 31 + delta, 1)])
    tables = {
        'patients': (['patient_id', 'age', 'sex', 'ward', 'severity', 'crp'], patients),
        'followup': (['patient_id', 'day', 'crp', 'status'], followup),
        'laboratory': (['sample_id', 'group', 'replicate', 'signal'], laboratory),
    }
    wb = Workbook(); wb.remove(wb.active)
    for name, (headers, rows) in tables.items():
        ws = wb.create_sheet(name); ws.append(headers)
        for row in rows: ws.append(row)
        ws.freeze_panes = 'A2'
        table = Table(displayName=name.title(), ref=ws.dimensions)
        table.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
        ws.add_table(table)
        for col in ws.columns: ws.column_dimensions[col[0].column_letter].width = 21
        with (DATA / f'M01_bank_{name}.csv').open('w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f); writer.writerow(headers); writer.writerows(rows)
    guide = wb.create_sheet('README')
    for row in [
        ['Synthetic educational data', 'No real patients; patterns are deterministic.'],
        ['patients', '1000 people; patient_id is unique.'],
        ['followup', '3000 planned visits; key is patient_id + day.'],
        ['laboratory', '100 independent samples; 2 technical readings each.'],
        ['Missing CRP in patients', 'IDs divisible by 20: 50 empty cells.'],
        ['Missing CRP in followup', 'day 0: 50; day 7: 100; all planned visits: 150.'],
        ['Warning', 'Designed for structure and missingness practice, not clinical inference.'],
        ['Codebook', 'See bank-codebook.md beside this workbook.'],
    ]: guide.append(row)
    guide.column_dimensions['A'].width=30; guide.column_dimensions['B'].width=85
    wb.save(DATA / 'M01_training_bank.xlsx')
    practice = Workbook(); ws=practice.active; ws.title='tasks'
    tasks=[
        ['Task', 'Your answer'],
        ['L1: Number of unique patients', None],
        ['L1: Number of planned follow-up visits', None],
        ['L2: Scale of severity; explain numeric codes', None],
        ['L3: Unique key of followup', None],
        ['L3: Number of independent laboratory samples', None],
        ['L4: Number of missing baseline CRP values', None],
        ['L4: Percent of day-7 CRP missing', None],
    ]
    for row in tasks: ws.append(row)
    ws.column_dimensions['A'].width=65; ws.column_dimensions['B'].width=60
    practice.save(DATA / 'M01_bank_practice.xlsx')
    answers = Workbook(); ws=answers.active; ws.title='answers'
    for row in [tasks[0], [tasks[1][0],1000],[tasks[2][0],3000],
                [tasks[3][0],'Ordinal; the codes do not establish equal spacing.'],
                [tasks[4][0],'patient_id + day'],[tasks[5][0],100],
                [tasks[6][0],50],[tasks[7][0],'10% = 100 / 1000; day-7 gaps / all visits: 100 / 3000; all gaps: 150 / 3000.']]:
        ws.append(row)
    ws.column_dimensions['A'].width=65; ws.column_dimensions['B'].width=70
    answers.save(DATA.parent / 'solutions/M01_bank_answers.xlsx')

if __name__ == '__main__':
    build()
