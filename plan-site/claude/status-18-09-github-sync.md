# סנכרון smart-home ל-GitHub — 18/09/2026

## מה נעשה
תיקיית `smart-home` המקומית של גיא (`<תיקיית smart-home המקומית>`, כוללת את `plan-site` ו-`landing-page`) הפכה ל-git repository ונדחפה ל-GitHub הפרטי של גיא:

- **Repo:** `https://github.com/guycohen85/smart-home` (private)
- **Branch:** `main` בלבד — הוסכם עם גיא לעבוד ישירות על `main` בכל commit (בלי branches נפרדים), כי ניתן תמיד לחזור אחורה עם `git revert`/`git reset` אם צריך.
- ה-repo כרגע מכיל commit ראשוני יחיד עם כל התוכן הקיים (11 קבצי HTML תחת plan-site + claude/decision-network-access.md, ו-3 קבצי landing-page).

## איך זה מוגדר טכנית
- Git מותקן על ה-Linux VM המקומי של גיא (נגיש דרך device_bash כשיש חיבור מכשיר).
- הרשאות: Personal Access Token (classic, scope `repo` + `project`) שגיא סיפק בצ'אט. הוגדר עם `git config credential.helper store` כך ש-git על אותו מכשיר יוכל לדחוף/למשוך בלי לבקש טוקן מחדש (בהנחה שה-VM המקומי נשמר בין הפעלות של אפליקציית הדסקטופ).
- הטוקן **לא** נשמר בקובץ כלשהו בתוך ה-repository עצמו, ולא נכתב כאן במסמך הזה מטעמי אבטחה.

## מה זה אומר להמשך עבודה
- **כשיש חיבור למחשב של גיא (desktop linked):** לעבוד ישירות על `$HOME/mnt/smart-home` דרך device_bash — לערוך קבצים במקום, ואז `git add -A && git commit -m "..." && git push` ישירות ל-`main`. אין צורך ב-staging/commit נפרדים לענן.
- **כשאין חיבור למחשב (למשל סשן מובייל טהור):** אין גישה אוטומטית ל-repo מהענן כרגע — צריך או שגיא יספק טוקן גישה מחדש כדי ש-Claude יוכל לשכפל את ה-repo בסביבת הענן, או להמתין לסשן עם חיבור למכשיר.
- כדאי לשקול בעתיד לחבר GitHub כ-connector רשמי (נבדק ב-18/09 — לא קיים כרגע ברשימת ה-connectors הזמינים לחשבון של גיא) כדי לקבל גישה עקבית מכל סוגי הסשנים בלי תלות בטוקן ידני.

## מה עוד לא הועלה
5 מסמכי `claude/*.md` הנוספים שמוזכרים ב-`status-18-09-merge.md` (decision-nabu-casa-services, idea-store-tosafot, status-16-09 וכו') ו-`claude/nabu-casa.html` — לא נבדק אם כולם קיימים בפועל תחת `plan-site/claude/` המקומי; רק `decision-network-access.md` נמצא שם בפועל בזמן הסנכרון.

*הערה: הנתיב המקומי המקורי הוסר מהמסמך מטעמי פרטיות, כי האתר מוגש דרך GitHub Pages.*
