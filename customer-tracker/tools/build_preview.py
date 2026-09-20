"""Builds index.html (mobile view of the workbook) from the recalculated xlsx.
Run after build_workbook.py + recalculation.
"""
import json
from pathlib import Path
from datetime import datetime, date
from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
wb = load_workbook(ROOT / 'onehome_customer_tracker_SAMPLE.xlsx', data_only=True)


def fmt(v):
    if v is None or v == '':
        return ''
    if isinstance(v, datetime):
        return v.strftime('%d/%m/%Y %H:%M') if (v.hour or v.minute) else v.strftime('%d/%m/%Y')
    if isinstance(v, date):
        return v.strftime('%d/%m/%Y')
    return v


def money(v):
    return '' if v in (None, '') else f'{v:,.0f} ₪'


MONEY = {'מחיר חבילה', 'ריטיינר חודשי', 'תוספות / הנחה (₪)', 'מחיר בפועל', 'עלות חומרה (כולל מע"מ)',
         'עלות חשמלאי', 'רווח התקנה (לפני שכר עצמי)', 'רווח התקנה לשעה'}
PERCENT = {'התקדמות checklist'}
HOURS = {'שעות התקנה (כולל נסיעות)', 'שעות תמיכה (ריטיינר)'}

c = wb['לקוחות']
H = [x.value for x in c[1]]
cust = []
for r in range(2, 22):
    row = [c.cell(r, i).value for i in range(1, len(H) + 1)]
    if not row[0]:
        continue
    out = []
    for h, v in zip(H, row):
        if h in MONEY:
            out.append(money(v))
        elif h in PERCENT:
            out.append('' if v in (None, '') else f'{v * 100:.0f}%')
        elif h in HOURS:
            out.append('' if v in (None, '') else f'{v:.1f}')
        else:
            out.append(fmt(v))
    cust.append(out)

k = wb['Checklist']
ids = [k.cell(1, i).value for i in range(3, 8)]
nc = len([x for x in ids if x])
last_item = max(r for r in range(2, 100) if k.cell(r, 1).value)
items = [{'g': k.cell(r, 1).value, 't': k.cell(r, 2).value, 'v': [k.cell(r, 3 + j).value or '' for j in range(nc)]}
         for r in range(2, last_item + 1)]
prog = [k.cell(last_item + 1, 3 + j).value for j in range(nc)]

h = wb['שעות']
hours = [[fmt(h.cell(r, i).value) for i in range(1, 6)] for r in range(2, 102) if h.cell(r, 1).value]
iss = wb['פניות']
issues = [[fmt(iss.cell(r, j).value) for j in range(1, 13)] for r in range(2, 102) if iss.cell(r, 1).value]
p = wb['חבילות']
pk = [[p.cell(r, 1).value, money(p.cell(r, 2).value), money(p.cell(r, 3).value)] for r in range(2, 5)]
sm = []
for r in range(9, 30):
    lab = p.cell(r, 1).value
    if not lab:
        break
    v = p.cell(r, 2).value
    sm.append([lab, money(v) if 'MRR' in lab else fmt(v)])
leg = [wb['הסבר'].cell(r, 1).value for r in range(1, wb['הסבר'].max_row + 1)]

data = {'H': H, 'cust': cust, 'ids': ids[:nc], 'items': items, 'prog': [f'{x * 100:.0f}%' for x in prog],
        'hours': hours, 'issues': issues, 'pk': pk, 'sm': sm, 'leg': leg}
tpl = (HERE / 'preview_template.html').read_text(encoding='utf-8')
(ROOT / 'index.html').write_text(tpl.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False)), encoding='utf-8')
print(len(cust), nc, len(items), len(hours), len(issues), len(sm))
