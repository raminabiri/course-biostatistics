"""Build the Excel workshop from the individual-level teaching CSV."""
from csv import reader
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

root = Path(__file__).resolve().parents[1]
book = Workbook()
data = book.active
data.title = "Data"
with (root / "data/M09_individuals.csv").open(encoding="utf-8") as stream:
    rows = reader(stream)
    data.append(next(rows))
    for person, population, reference, test, joint_code in rows:
        data.append([int(person), population, reference, test, int(joint_code)])
data.freeze_panes = "B2"
data.auto_filter.ref = data.dimensions
analysis = book.create_sheet("Analysis")
book.active = 1
for sheet in (data, analysis):
    sheet.sheet_view.rightToLeft = True
    for column in "ABCDEFGHI":
        sheet.column_dimensions[column].width = 23

for start, title in [("A", "baseline"), ("E", "low")]:
    offset = ord(start) - ord("A")
    analysis.cell(1, offset + 1, title)
    for idx, label in enumerate(["مثبت", "منفی", "جمع"], offset + 2):
        analysis.cell(2, idx, label)
    for row, label in [(3, "بیماری دارد"), (4, "بیماری ندارد"), (5, "جمع")]:
        analysis.cell(row, offset + 1, label)
    positive = chr(ord(start) + 1)
    negative = chr(ord(start) + 2)
    total = chr(ord(start) + 3)
    for row, ref in [(3, "positive"), (4, "negative")]:
        for col, test in [(positive, "positive"), (negative, "negative")]:
            analysis[f"{col}{row}"] = (
                f'=COUNTIFS(Data!$B$2:$B$11001,${start}$1,'
                f'Data!$C$2:$C$11001,"{ref}",Data!$D$2:$D$11001,"{test}")'
            )
        analysis[f"{total}{row}"] = f"=SUM({positive}{row}:{negative}{row})"
    for col in (positive, negative, total):
        analysis[f"{col}5"] = f"=SUM({col}3:{col}4)"
    for row, label, formula in [
        (7, "بیمار یا مثبت", f"=1-{negative}4/{total}5"),
        (8, "مثبت در بیماران", f"={positive}3/{total}3"),
        (9, "بیمار در مثبت‌ها", f"={positive}3/{positive}5"),
    ]:
        analysis[f"{start}{row}"] = label
        analysis[f"{positive}{row}"] = formula
        analysis[f"{positive}{row}"].number_format = "0.00%"

analysis.append([])
analysis.append([])
for col, name in enumerate([
    "جمعیت", "شیوع", "حساسیت", "ویژگی", "سهم مثبت واقعی", "سهم مثبت کاذب",
    "PPV بیز", "PPV شمار مستقیم", "تفاوت مدل و شمار"
], 1):
    analysis.cell(12, col, name)
for row, name, col_total, col_positive in [(13,"baseline","D","B"),(14,"low","H","F")]:
    for col, val in enumerate([
        name, f"={col_total}3/{col_total}5", "=$B$8", "=$C$4/$D$4",
        f"=B{row}*C{row}", f"=(1-B{row})*(1-D{row})",
        f"=E{row}/SUM(E{row}:F{row})", f"={col_positive}9", f"=G{row}-H{row}",
    ], 1):
        analysis.cell(row, col, val)
        if col > 1:
            analysis.cell(row, col).number_format = "0.0000%"
for sheet, rows in [(data, (1,)), (analysis, (1,2,12))]:
    for row in rows:
        for cell in sheet[row]:
            if cell.value is not None:
                cell.fill = PatternFill("solid", fgColor="18576A")
                cell.font = Font(color="FFFFFF", bold=True)
book.save(root / "excel/M09_workshop.xlsx")
