# סטטוס מיזוג — 18/09/2026: plan-site הפך למקור האמת היחיד

## מה קרה
התגלה שה-Project docs (כאן ב-Claude) ותיקיית `plan-site` המקומית של גיא (`<תיקיית smart-home המקומית>\plan-site`) התפצלו לשני היסטוריות עריכה נפרדות:

- **התעדכן רק כאן בפרויקט:** `vision.html`, `products.html`, `index.html` — עדכוני Nabu Casa/גישה מרחוק (הסרת Cloudflare Tunnel מצד הלקוח, מחיר עדכני, Internal/External URL).
- **התעדכן רק מקומית ב-plan-site:** `prd1.html`, `prd4.html` — רפקטור Watchman (הועבר מ-PRD1 ל-PRD4). וגם שלושה דפים שהיו קיימים רק מקומית ולא הועלו לכאן מעולם: `automations.html`, `kb.html`, `prd5.html`.
- `competitors.html`, `prds.html`, `prd2.html` — כמעט זהים בשני המקורות, רק תפריט הניווט היה שונה.

## מה נעשה
בוצע מיזוג מלא, קובץ-קובץ (באמצעות `diff` אמיתי, לא רק תאריכי קבצים), ו-plan-site עודכן עם התוכן המלא והנכון ביותר מכל מקור, כולל תפריט ניווט אחיד לכל 8 הדפים (בית / חזון / מוצרים / מתחרים / PRD-ים / ידע טכני / אוטומציות / Nabu Casa). גם תוקן פסקה מיושנת ב-`kb.html` שעדיין תיארה Nabu Casa/Cloudflare Tunnel כ"רכיב חובה" — עודכנה לשקף את ההחלטה הנוכחית (ברירת מחדל: גישה מקומית בלבד; Nabu Casa = תוספת אופציונלית בתשלום).

**plan-site הוא כעת מקור האמת היחיד** לכל 11 דפי ה-HTML + `claude/nabu-casa.html`.

## מה קרה ל-8 המסמכים הכפולים בפרויקט
לפי בקשת גיא, 8 המסמכים שהיו כפולים (`competitors.html`, `index.html`, `prd1.html`, `prd2.html`, `prd4.html`, `prds.html`, `products.html`, `vision.html`) **לא נמחקו ישירות** — הם הועברו לנתיב `need-review-before-delete/` בפרויקט (עם הערה על מה היה בכל אחד ולמה הוא מיושן/מיותר), כדי שגיא יוכל לעיין ולמחוק בעצמו.

## מה עדיין נשאר כפול בפרויקט (טרם טופל)
5 מסמכי `claude/*.md` (`decision-nabu-casa-services.md`, `decision-network-access.md`, `idea-store-tosafot.md`, `status-16-09.md`) וגם `claude/nabu-casa.html` — עדיין קיימים גם כאן בפרויקט וגם ב-plan-site (תחת `plan-site/claude/`). לא הועברו/נמחקו כי גיא לא נשאל עליהם ספציפית — רק על 8 קבצי ה-HTML הראשיים.

*הערה: הנתיב המקומי המקורי הוסר מהמסמך מטעמי פרטיות, כי האתר מוגש דרך GitHub Pages.*
