"""Builds the SAMPLE customer tracking workbook (fictional customer C001).
Run: python3 build_workbook.py  — then recalculate (see ../README.md) so cached values exist.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment
from datetime import date, datetime
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'onehome_customer_tracker_SAMPLE.xlsx'
SUPPORT = 'תמיכה (ריטיינר)'

F = 'Arial'
BLUE = Font(name=F, size=10, color='0000FF')
BLK = Font(name=F, size=10, color='000000')
BOLD = Font(name=F, size=10, bold=True)
HDR = Font(name=F, size=10, bold=True, color='FFFFFF')
HFILL = PatternFill('solid', fgColor='0F172A')
GFILL = PatternFill('solid', fgColor='E5E7EB')   # formula cells
thin = Side(style='thin', color='CBD5E1'); BRD = Border(left=thin, right=thin, top=thin, bottom=thin)
CEN = Alignment(horizontal='center', vertical='center', wrap_text=True)
RGT = Alignment(horizontal='right', vertical='center', wrap_text=True)
DATE = 'DD/MM/YYYY'; DT = 'DD/MM/YYYY HH:MM'
ILS = '#,##0 "₪"'; ILS_NEG = '#,##0 "₪";[Red]-#,##0 "₪"'

wb = Workbook()
ws_leg = wb.active; ws_leg.title = 'הסבר'
ws_c = wb.create_sheet('לקוחות'); ws_k = wb.create_sheet('Checklist')
ws_h = wb.create_sheet('שעות'); ws_i = wb.create_sheet('פניות'); ws_p = wb.create_sheet('חבילות')
for ws in wb.worksheets:
    ws.sheet_view.rightToLeft = True


def header(ws, row, names, widths=None):
    for i, n in enumerate(names, 1):
        c = ws.cell(row=row, column=i, value=n); c.font = HDR; c.fill = HFILL; c.alignment = CEN; c.border = BRD
    ws.row_dimensions[row].height = 40
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[L(i)].width = w


# ---------------- לקוחות: column definitions (letters are derived, never hard-coded) ----------------
CUST = [
    ('id', 'מזהה לקוח', 10), ('name', 'שם לקוח', 22), ('phone', 'טלפון', 14), ('city', 'עיר / אזור', 14),
    ('pkg', 'חבילה', 12), ('list_price', 'מחיר חבילה', 12), ('retainer', 'ריטיינר חודשי', 12),
    ('adj', 'תוספות / הנחה (₪)', 13), ('price', 'מחיר בפועל', 12),
    ('d_survey', 'תאריך סקר בית', 13), ('d_install', 'תאריך התקנה', 13), ('d_accept', 'תאריך אישור קבלה', 14),
    ('ret_start', 'תחילת ריטיינר (= אישור קבלה)', 16), ('status', 'סטטוס', 14),
    ('ip', 'IP קבוע', 14), ('mac', 'MAC של ה-HA', 20), ('ha_ver', 'גרסת HA', 11),
    ('nabu', 'Nabu Casa', 10), ('nabu_svc', 'שירותי Nabu Casa שנבחרו', 24),
    ('r2', 'שם bucket ב-R2', 24), ('monitor', 'מזהה ניטור', 18),
    ('elec_work', 'עבודת חשמל', 11), ('electrician', 'חשמלאי', 16),
    ('hw_cost', 'עלות חומרה (כולל מע"מ)', 14), ('elec_cost', 'עלות חשמלאי', 12),
    ('profit', 'רווח התקנה (לפני שכר עצמי)', 15), ('progress', 'התקדמות checklist', 13),
    ('hours', 'שעות התקנה (כולל נסיעות)', 14), ('pph', 'רווח התקנה לשעה', 13),
    ('support', 'שעות תמיכה (ריטיינר)', 13), ('open_issues', 'פניות פתוחות', 10),
    ('secrets', 'הפניה לסודות (מנהל סיסמאות)', 30), ('notes', 'הערות', 30),
]
KEYS = [k for k, _, _ in CUST]
def col(k): return L(KEYS.index(k) + 1)
def idx(k): return KEYS.index(k) + 1
FORMULA_KEYS = {'list_price', 'retainer', 'price', 'ret_start', 'profit', 'progress', 'hours', 'pph', 'support', 'open_issues'}
FIRST, LAST = 2, 21   # customer rows with ready formulas
N_CHECK_CUSTOMERS = 5

# ---------------- חבילות ----------------
header(ws_p, 1, ['חבילה', 'מחיר התקנה (₪)', 'ריטיינר חודשי (₪)'], [34, 18, 18])
for r, (n, a, b) in enumerate([('EcoHome', 5700, 160), ('SafeHome', 8700, 220), ('EliteHome', 13150, 350)], 2):
    ws_p.cell(r, 1, n).font = BLK
    for c_, v in ((2, a), (3, b)):
        c = ws_p.cell(r, c_, v); c.font = BLUE; c.number_format = ILS
    for c_ in (1, 2, 3):
        ws_p.cell(r, c_).border = BRD
ws_p['A6'] = 'מקור המחירים: PRD 1 / תמחור מעודכן ב-16/09/2026. אם התמחור משתנה — לעדכן כאן בלבד (תאים כחולים).'
ws_p['A6'].font = Font(name=F, size=9, italic=True, color='475569')
ws_p['A8'] = 'סיכום'; ws_p['A8'].font = BOLD
st = f"'לקוחות'!${col('status')}${FIRST}:${col('status')}${LAST}"
rt = f"'לקוחות'!${col('retainer')}${FIRST}:${col('retainer')}${LAST}"
summ = [
    ('לקוחות פעילים', f'=COUNTIF({st},"פעיל")', '0'),
    ('הכנסה חודשית מריטיינר (MRR)', f'=SUMIFS({rt},{st},"פעיל")', ILS),
    ('סה"כ פניות פתוחות', "=COUNTIF('פניות'!$F$2:$F$500,\"פתוחה\")", '0'),
    ('אירועים קריטיים מעבר ל-SLA (יעד: 0)', "=COUNTIFS('פניות'!$E$2:$E$500,\"קריטי\",'פניות'!$K$2:$K$500,\"✗\")", '0'),
    ('סה"כ שעות התקנה (ללא תמיכה)', f"=SUM('שעות'!$D$2:$D$500)-SUMIFS('שעות'!$D$2:$D$500,'שעות'!$B$2:$B$500,\"{SUPPORT}\")", '0.0'),
    ('סה"כ שעות תמיכה', f"=SUMIFS('שעות'!$D$2:$D$500,'שעות'!$B$2:$B$500,\"{SUPPORT}\")", '0.0'),
]
for k, (lab, fm, nf) in enumerate(summ, 9):
    ws_p.cell(k, 1, lab).font = BLK
    c = ws_p.cell(k, 2, fm); c.font = BLK; c.fill = GFILL; c.number_format = nf; c.border = BRD

# ---------------- לקוחות ----------------
header(ws_c, 1, [h for _, h, _ in CUST], [w for _, _, w in CUST])
for r in range(FIRST, LAST + 1):
    a = f'$A{r}'
    fm = {
        'list_price': f'=IF($E{r}="","",IFERROR(INDEX(\'חבילות\'!$B$2:$B$4,MATCH($E{r},\'חבילות\'!$A$2:$A$4,0)),""))',
        'retainer': f'=IF($E{r}="","",IFERROR(INDEX(\'חבילות\'!$C$2:$C$4,MATCH($E{r},\'חבילות\'!$A$2:$A$4,0)),""))',
        'price': f'=IF(OR({a}="",${col("list_price")}{r}=""),"",${col("list_price")}{r}+N(${col("adj")}{r}))',
        'ret_start': f'=IF(${col("d_accept")}{r}="","",${col("d_accept")}{r})',
        'profit': f'=IF(OR({a}="",${col("price")}{r}="",${col("hw_cost")}{r}=""),"",${col("price")}{r}-${col("hw_cost")}{r}-N(${col("elec_cost")}{r}))',
        'progress': f"=IF({a}=\"\",\"\",IFERROR(INDEX('Checklist'!$C$CHKROW:${L(2 + N_CHECK_CUSTOMERS)}$CHKROW,MATCH({a},'Checklist'!$C$1:${L(2 + N_CHECK_CUSTOMERS)}$1,0)),\"\"))",
        'hours': f"=IF({a}=\"\",\"\",SUMIFS('שעות'!$D$2:$D$500,'שעות'!$A$2:$A$500,{a})-SUMIFS('שעות'!$D$2:$D$500,'שעות'!$A$2:$A$500,{a},'שעות'!$B$2:$B$500,\"{SUPPORT}\"))",
        'pph': f'=IF({a}="","",IFERROR(${col("profit")}{r}/${col("hours")}{r},""))',
        'support': f"=IF({a}=\"\",\"\",SUMIFS('שעות'!$D$2:$D$500,'שעות'!$A$2:$A$500,{a},'שעות'!$B$2:$B$500,\"{SUPPORT}\"))",
        'open_issues': f"=IF({a}=\"\",\"\",COUNTIFS('פניות'!$B$2:$B$500,{a},'פניות'!$F$2:$F$500,\"פתוחה\"))",
    }
    for k, f_ in fm.items():
        ws_c.cell(r, idx(k)).value = f_   # CHKROW placeholder replaced after checklist is laid out
    for c in range(1, len(CUST) + 1):
        cell = ws_c.cell(r, c); cell.border = BRD; cell.alignment = RGT
        if KEYS[c - 1] in FORMULA_KEYS:
            cell.font = BLK; cell.fill = GFILL
        else:
            cell.font = BLUE
    for k in ('list_price', 'retainer', 'adj', 'price', 'hw_cost', 'elec_cost'):
        ws_c.cell(r, idx(k)).number_format = ILS
    for k in ('profit', 'pph'):
        ws_c.cell(r, idx(k)).number_format = ILS_NEG
    for k in ('d_survey', 'd_install', 'd_accept', 'ret_start'):
        ws_c.cell(r, idx(k)).number_format = DATE
    ws_c.cell(r, idx('progress')).number_format = '0%'
    for k in ('hours', 'support'):
        ws_c.cell(r, idx(k)).number_format = '0.0'

sample = {
    'id': 'C001', 'name': 'לקוח לדוגמה (לא אמיתי)', 'phone': '050-0000000', 'city': 'תל אביב', 'pkg': 'SafeHome',
    'adj': 0, 'd_survey': date(2026, 10, 5), 'd_install': date(2026, 10, 19), 'd_accept': date(2026, 10, 19),
    'status': 'פעיל', 'ip': '192.168.1.50', 'mac': 'AA:BB:CC:DD:EE:FF', 'ha_ver': '2026.9.3', 'nabu': 'לא', 'nabu_svc': '—',
    'r2': 'onehome-c001-backups', 'monitor': 'c001-sample', 'elec_work': 'כן', 'electrician': 'חשמלאי א׳ (לדוגמה)',
    'hw_cost': 4200, 'elec_cost': 800,
    'secrets': 'Bitwarden: OneHome/C001 (לדוגמה)', 'notes': 'נתוני דוגמה בלבד — למחוק את השורה לפני שימוש אמיתי',
}
for k, v in sample.items():
    ws_c.cell(FIRST, idx(k), v)
ws_c.freeze_panes = 'C2'


def dv(ws, formula, rng):
    d = DataValidation(type='list', formula1=formula, allow_blank=True); ws.add_data_validation(d); d.add(rng)
rng = lambda k: f'{col(k)}{FIRST}:{col(k)}{LAST}'
dv(ws_c, "='חבילות'!$A$2:$A$4", rng('pkg'))
dv(ws_c, '"ליד,סקר בית,הצעה נשלחה,הזמנת ציוד,התקנה,בדיקות קבלה,פעיל,מושהה,הופסק"', rng('status'))
dv(ws_c, '"כן,לא"', rng('nabu')); dv(ws_c, '"כן,לא"', rng('elec_work'))
ws_c[f"{col('progress')}1"].comment = Comment(f'מחושב אוטומטית מלשונית Checklist. מופיע רק ללקוחות בשורות 2–{1 + N_CHECK_CUSTOMERS}.', 'Claude')
ws_c[f"{col('hours')}1"].comment = Comment(f'סכום כל השעות של הלקוח בלשונית שעות, חוץ מהשלב "{SUPPORT}" (זה נספר בעמודה נפרדת).', 'Claude')
ws_c[f"{col('profit')}1"].comment = Comment('מחיר בפועל פחות עלות חומרה ופחות עלות חשמלאי. לא כולל שכר עצמי ועלויות כלים חודשיות (R2, ניטור).', 'Claude')
ws_c[f"{col('monitor')}1"].comment = Comment('מזהה כללי, מתאים לכל כלי ניטור שיוחלט עליו (למשל שם environment או מזהה של דופק). עוד לא הוחלט על הכלי.', 'Claude')

# ---------------- Checklist ----------------
items = [
    ('רשת וגישה מקומית', ['AP/Client Isolation כבוי בראוטר', 'רשת שטוחה אחת (או VLAN מאושר ללקוח מיוחד)', 'DHCP Reservation לפי MAC בראוטר', 'Internal URL מוגדר לפי ה-IP הקבוע', 'אפליקציית Companion מזהה את ה-SSID הביתי', 'גישת אדמין לראוטר אומתה לפני ההתקנה']),
    ('Nabu Casa (רק אם הלקוח בחר)', ['הלקוח פתח חשבון בשמו ובכרטיס שלו', 'External URL מוגדר', 'שירותים נבחרו בנפרד (Alexa/Google, גיבוי ענן, Webhooks)', 'TTS/STT ענני — החלטה מוצהרת (ברירת מחדל: מקומי)', 'WebRTC למצלמות — החלטה מוצהרת (ברירת מחדל: כבוי)']),
    ('פרטיות וגיבויים', ['מסמך פרטיות נחתם', 'bucket מבודד ב-R2 נוצר', 'סיסמת הצפנה ייחודית נשמרה במנהל סיסמאות', 'גיבוי ראשון הצליח ל-R2', 'עותק גיבוי מקומי נשמר בבית']),
    ('בדיקות קבלה — "הבית חי"', ['כל מכשירי החבילה מחוברים, בשמות ברורים ופועלים', 'בדיקת ניתוק אינטרנט: אוטומציה מקומית ממשיכה לרוץ', 'Push בדיקה התקבל בטלפון הלקוח מחוץ ל-WiFi הביתי', 'חיישן הצפה נבדק (מים על החיישן מפעילים התראה)', 'גלאי עשן וסירנה מקומית נבדקו', 'כניסה מרחוק מדאטה סלולרי (אם נרכשה גישה מרחוק)', 'הלקוח ביצע בעצמו פעולה אחת (אור / פתיחת קריאה)', 'ניטור Alert פועל', 'IP, MAC וגרסת HA נרשמו בלשונית לקוחות']),
    ('חוזי ומסירה', ['אישור כתוב מהחשמלאי (אם הייתה עבודת חשמל)', 'חבילת מסירה נמסרה ללקוח', 'אישור קבלה חתום — מתחיל ריטיינר ו-SLA']),
]
n_items = sum(len(x) for _, x in items)
CHK_LAST = 1 + n_items        # last item row
CHK_PROG = CHK_LAST + 1       # progress row
last_col = L(2 + N_CHECK_CUSTOMERS)
header(ws_k, 1, ['קבוצה', 'פריט'] + [''] * N_CHECK_CUSTOMERS, [26, 58] + [12] * N_CHECK_CUSTOMERS)
for j in range(N_CHECK_CUSTOMERS):
    c = ws_k.cell(1, 3 + j, f"=IF('לקוחות'!$A{FIRST + j}=\"\",\"\",'לקוחות'!$A{FIRST + j})")
    c.font = HDR; c.fill = HFILL; c.alignment = CEN; c.border = BRD
r = 2
for grp, its in items:
    for it in its:
        ws_k.cell(r, 1, grp).font = Font(name=F, size=9, color='64748B'); ws_k.cell(r, 2, it).font = BLK
        for c in range(1, 3 + N_CHECK_CUSTOMERS):
            ws_k.cell(r, c).border = BRD; ws_k.cell(r, c).alignment = RGT if c < 3 else CEN
        for c in range(3, 3 + N_CHECK_CUSTOMERS):
            ws_k.cell(r, c).font = BLUE
        v = '✓'
        if grp.startswith('Nabu Casa') or 'דאטה סלולרי' in it:
            v = 'לא רלוונטי'
        ws_k.cell(r, 3, v)
        r += 1
assert r - 1 == CHK_LAST
ws_k.cell(CHK_PROG, 2, 'התקדמות (לא כולל "לא רלוונטי")').font = BOLD
for c in range(3, 3 + N_CHECK_CUSTOMERS):
    cl = L(c)
    cell = ws_k.cell(CHK_PROG, c, f'=IF({cl}$1="","",COUNTIF({cl}2:{cl}{CHK_LAST},"✓")/MAX(1,ROWS({cl}2:{cl}{CHK_LAST})-COUNTIF({cl}2:{cl}{CHK_LAST},"לא רלוונטי")))')
    cell.font = BLK; cell.fill = GFILL; cell.number_format = '0%'; cell.alignment = CEN; cell.border = BRD
ws_k.cell(CHK_PROG, 1).border = BRD; ws_k.cell(CHK_PROG, 2).border = BRD
ws_k.freeze_panes = 'C2'
area = f'C2:{last_col}{CHK_LAST}'
dv(ws_k, '"✓,✗,לא רלוונטי"', area)
for val, color in (('"✓"', 'D1FAE5'), ('"✗"', 'FEE2E2'), ('"לא רלוונטי"', 'E5E7EB')):
    ws_k.conditional_formatting.add(area, CellIsRule(operator='equal', formula=[val], fill=PatternFill('solid', bgColor=color)))
# now that the progress row is known, finish the customers formulas
for rr in range(FIRST, LAST + 1):
    c = ws_c.cell(rr, idx('progress')); c.value = c.value.replace('CHKROW', str(CHK_PROG))

# ---------------- שעות ----------------
header(ws_h, 1, ['מזהה לקוח', 'שלב', 'תאריך', 'שעות בפועל', 'הערה'], [12, 26, 13, 13, 44])
phases = ['פגישת מכירה', 'סקר בית', 'הצעה וחתימה', 'הכנה אצל גיא', 'עבודת חשמל (ליווי)', 'נסיעות', 'התקנה ורשת', 'בדיקות קבלה', 'מסירה והדרכה', SUPPORT]
rows = [('C001', 'פגישת מכירה', date(2026, 9, 28), 1.5, 'פגישה ראשונה בבית הלקוח'),
        ('C001', 'נסיעות', date(2026, 9, 28), 1, ''),
        ('C001', 'סקר בית', date(2026, 10, 5), 2, ''),
        ('C001', 'נסיעות', date(2026, 10, 5), 1, ''),
        ('C001', 'הצעה וחתימה', date(2026, 10, 8), 1.5, 'כולל מסמך פרטיות'),
        ('C001', 'הכנה אצל גיא', date(2026, 10, 14), 3, 'HA, R2, גיבוי ראשון'),
        ('C001', 'נסיעות', date(2026, 10, 19), 1, ''),
        ('C001', 'התקנה ורשת', date(2026, 10, 19), 5, ''),
        ('C001', 'בדיקות קבלה', date(2026, 10, 19), 1.5, ''),
        ('C001', 'מסירה והדרכה', date(2026, 10, 19), 1, ''),
        ('C001', SUPPORT, date(2026, 10, 21), 1, 'פנייה P001'),
        ('C001', SUPPORT, date(2026, 11, 2), 0.5, 'פנייה P002')]
for r in range(2, 102):
    for c in range(1, 6):
        cell = ws_h.cell(r, c); cell.font = BLUE; cell.border = BRD; cell.alignment = RGT
    ws_h.cell(r, 3).number_format = DATE; ws_h.cell(r, 4).number_format = '0.0'
for i, row in enumerate(rows, 2):
    for c, v in enumerate(row, 1):
        ws_h.cell(i, c, v)
dv(ws_h, '"' + ','.join(phases) + '"', 'B2:B101')
ws_h.freeze_panes = 'A2'
ws_h['G1'] = f'שורה לכל שלב עבודה. הסכום לכל לקוח מוצג בלשונית לקוחות. השלב "{SUPPORT}" נספר בנפרד משעות ההתקנה.'
ws_h['G1'].font = Font(name=F, size=9, italic=True, color='475569'); ws_h.column_dimensions['G'].width = 60

# ---------------- פניות ----------------
header(ws_i, 1, ['מזהה פנייה', 'מזהה לקוח', 'תאריך פתיחה', 'נושא', 'חומרה', 'סטטוס', 'תגובה ראשונה', 'תאריך פתרון', 'זמן פתרון (שעות)', 'יעד SLA לתגובה', 'עמד ב-SLA?', 'הערות'],
       [12, 12, 17, 44, 12, 12, 17, 17, 13, 17, 12, 40])
for r in range(2, 102):
    for c in range(1, 13):
        cell = ws_i.cell(r, c); cell.border = BRD; cell.alignment = RGT
        cell.font = BLK if c in (9, 10, 11) else BLUE
        if c in (9, 10, 11):
            cell.fill = GFILL
    for c in (3, 7, 8, 10):
        ws_i.cell(r, c).number_format = DT
    ws_i.cell(r, 9).number_format = '0.0'
    ws_i.cell(r, 9).value = f'=IF(OR($C{r}="",$H{r}=""),"",ROUND(($H{r}-$C{r})*24,1))'
    ws_i.cell(r, 10).value = f'=IF(OR($C{r}="",$E{r}="",$E{r}="בקשה"),"",WORKDAY.INTL(INT($C{r}),IF($E{r}="קריטי",1,3),7)+1-1/1440)'
    ws_i.cell(r, 11).value = f'=IF($J{r}="","",IF($G{r}="","טרם נענה",IF($G{r}<=$J{r},"✓","✗")))'
samp = [('P001', 'C001', datetime(2026, 10, 21, 9, 10), 'התראת הצפה לא הגיעה לטלפון של בת הזוג', 'קריטי', 'סגורה', datetime(2026, 10, 21, 9, 40), datetime(2026, 10, 21, 11, 40), 'נתוני דוגמה — הוגדרה מחדש הרשאת התראות באפליקציה'),
        ('P002', 'C001', datetime(2026, 11, 2, 18, 0), 'שאלה על הוספת מנורה לדשבורד', 'בקשה', 'פתוחה', None, None, 'נתוני דוגמה')]
for i, row in enumerate(samp, 2):
    for c, v in zip((1, 2, 3, 4, 5, 6, 7, 8, 12), row):
        ws_i.cell(i, c, v)
dv(ws_i, '"קריטי,אזהרה,בקשה"', 'E2:E101')
dv(ws_i, '"פתוחה,סגורה"', 'F2:F101')
ws_i.freeze_panes = 'A2'
ws_i['J1'].comment = Comment('סוף יום העסקים ה-N אחרי הפתיחה (ימי עסקים א׳–ה׳, בלי חגים): קריטי = יום 1, אזהרה = 3 ימים. "בקשה" ללא SLA. לפי PRD 1, סעיף E.', 'Claude')
ws_i.conditional_formatting.add('K2:K101', CellIsRule(operator='equal', formula=['"✓"'], fill=PatternFill('solid', bgColor='D1FAE5')))
ws_i.conditional_formatting.add('K2:K101', CellIsRule(operator='equal', formula=['"✗"'], fill=PatternFill('solid', bgColor='FEE2E2')))

# ---------------- הסבר ----------------
ws_leg.column_dimensions['A'].width = 110
lines = [
    ('OneHome — גיליון מעקב לקוחות (קובץ דוגמה)', True),
    ('הקובץ הזה מכיל נתוני דוגמה בלבד (לקוח C001, לא אמיתי). כדי להשתמש בו: לשמור עותק במקום פרטי, למחוק את שורת הדוגמה בכל לשונית, ולהתחיל למלא.', False),
    ('', False),
    ('איך לקרוא את הצבעים', True),
    ('טקסט כחול = תא שממלאים ידנית.   טקסט שחור על רקע אפור = נוסחה, לא לערוך.', False),
    ('', False),
    ('הלשוניות', True),
    ('לקוחות — שורה לכל לקוח. נוסחאות מוכנות עד שורה 21. כולל מחיר בפועל, עלות חומרה וחשמלאי, רווח לשעה, שעות תמיכה ומזהה ניטור. שדות ה-IP, MAC, R2 ומזהה הניטור הם אלה ש-PRD 4 (כלי ניהול פנימי) יצטרך, כך שבהמשך אפשר לייבא אותם.', False),
    ('Checklist — עמודה לכל לקוח, נמשכת אוטומטית מלשונית לקוחות (5 הלקוחות הראשונים). מבוסס על PRD 3, סעיפים B ו-D. "לא רלוונטי" לא נספר באחוז ההתקנה.', False),
    (f'שעות — שורה לכל שלב עבודה, כולל "נסיעות". השלב "{SUPPORT}" נספר בנפרד, כדי לראות כמה תמיכה כל לקוח באמת צורך מול הריטיינר שלו.', False),
    ('פניות — יומן פניות אחרי המסירה. חומרה לפי PRD 1: קריטי (תגובה עד יום עסקים), אזהרה (עד 3 ימי עסקים), בקשה (ללא SLA). "מידע" לא נרשם, כי גיא לא מעורב.', False),
    ('חבילות — מחירי ההתקנה והריטיינר (מקור: PRD 1, 16/09/2026) וסיכום: לקוחות פעילים, הכנסה חודשית, פניות פתוחות, אירועים קריטיים מעבר ל-SLA ושעות עבודה.', False),
    ('', False),
    ('כללים חשובים', True),
    ('1. אין סודות בקובץ. סיסמאות WiFi, סיסמאות אדמין של HA וסיסמת הצפנת הגיבויים — רק במנהל סיסמאות. בעמודה "הפניה לסודות" כותבים איפה הם שמורים.', False),
    ('2. לא לשמור את הקובץ האמיתי ב-repo של smart-home או ב-plan-site (האתר ב-GitHub Pages עלול להיות נגיש ברשת) ולא בחשבון OneDrive של המעסיק.', False),
    ('3. "רווח התקנה" = מחיר בפועל − עלות חומרה − עלות חשמלאי. "רווח לשעה" = רווח התקנה ÷ שעות התקנה (כולל נסיעות). שניהם לפני שכר עצמי ולפני עלויות כלים חודשיות (R2, ניטור).', False),
    ('4. תחילת ריטיינר = תאריך אישור קבלה חתום (החלטה ב-PRD 3, סעיף B).', False),
    ('5. "מזהה ניטור" הוא עמודה כללית — עוד לא הוחלט איזה כלי ניטור ישמש (Sentry, דופק או אחר).', False),
    ('6. בדיקת ה-SLA מניחה ימי עסקים א׳–ה׳ בלי חגים, והיעד הוא סוף יום העסקים ה-N אחרי פתיחת הפנייה. אם שישי נחשב יום עסקים, לתקן את הנוסחה בעמודה "יעד SLA".', False),
]
for i, (t, b) in enumerate(lines, 1):
    c = ws_leg.cell(i, 1, t); c.font = Font(name=F, size=12 if i == 1 else 10, bold=b)
    c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='right')
wb.save(OUT)
print('saved', OUT)
