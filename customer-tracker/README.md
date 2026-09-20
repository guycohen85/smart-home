# גיליון מעקב לקוחות — OneHome

תיקייה זו מכילה **קובץ דוגמה בלבד** (לקוח C001 פיקטיבי). היא נועדה להחליט איך הגיליון ייראה לפני שנבנה את כלי הניהול הפנימי (PRD 4).

## מה יש כאן

| קובץ | מה זה |
|---|---|
| `onehome_customer_tracker_SAMPLE.xlsx` | הגיליון עצמו, 6 לשוניות: לקוחות, Checklist, שעות, פניות, חבילות, הסבר |
| `preview.html` | תצוגה לטלפון של אותו גיליון (כרטיסים במקום 27 עמודות). אמורה להיות נגישה ב-`https://guycohen85.github.io/smart-home/customer-tracker/preview.html` |
| `tools/build_workbook.py` | יוצר מחדש את האקסל. שינויים בגיליון נעשים כאן, לא ידנית באקסל, כדי שהקבצים יישארו זהים |
| `tools/build_preview.py` + `tools/preview_template.html` | יוצרים מחדש את `preview.html` מתוך האקסל |

## איך מעדכנים

```bash
cd customer-tracker/tools
python3 build_workbook.py                 # יוצר את האקסל
# חישוב מחדש של הנוסחאות (LibreOffice), כדי שיישמרו ערכים מחושבים בקובץ:
soffice --headless --convert-to xlsx --outdir /tmp/recalc ../onehome_customer_tracker_SAMPLE.xlsx
cp /tmp/recalc/onehome_customer_tracker_SAMPLE.xlsx ..
python3 build_preview.py                  # יוצר את preview.html
```

דרישות: `openpyxl` ו-LibreOffice.

## כללים

1. **אין סודות בגיליון.** סיסמאות WiFi, סיסמאות אדמין של HA וסיסמת הצפנת הגיבויים — רק במנהל סיסמאות. בגיליון רק הפניה לאיפה הם שמורים.
2. **הקובץ האמיתי לא נשמר ב-repo הזה.** GitHub Pages מגיש את כל ה-repo, ולכן פרטי לקוחות אמיתיים לא שייכים לכאן. `.gitignore` חוסם `customer-tracker/real/` וקבצים ששמם כולל `_REAL`.
3. **לא בחשבון OneDrive של המעסיק.** לשמור את הקובץ האמיתי בחשבון Google או OneDrive אישי.

## קשר למסמכים אחרים

- ההגדרה של "הבית חי" וה-checklist: `plan-site/prd3.html`
- שדות ה-IP, MAC, R2 ו-Sentry תואמים למה ש-`plan-site/prd4.html` (כלי ניהול פנימי) יצטרך, כך שבהמשך אפשר לייבא אותם.
- מחירי החבילות: `plan-site/prd1.html` (עדכון 16/09/2026).
