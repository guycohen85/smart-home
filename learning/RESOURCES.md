# משאבים ל-Home Assistant / OneHome

מקורות אמינים ללמידה. ידע לשיעורים נשאב מכאן ומתוך `plan-site` (הידע הפנימי שגיא כבר צבר) — לא מזיכרון כללי.

## Knowledge — כלליים (Home Assistant)

- [Home Assistant — Getting Started](https://www.home-assistant.io/getting-started/)
  התיעוד הרשמי, נקודת ההתחלה הרשמית להתקנה ולשימוש בסיסי. המקור הראשי למסלול הלקוח.
- [Home Assistant — Concepts and terminology](https://www.home-assistant.io/getting-started/concepts-terminology/)
  ההגדרה הרשמית של Entity / Device / Area / Integration. המקור לשיעור 0001 (מפת המושגים).
- [Home Assistant — Glossary](https://www.home-assistant.io/docs/glossary/)
  מילון מונחים רשמי — שימושי כרפרנס מהיר תוך כדי עבודה.
- [Home Assistant — Areas](https://www.home-assistant.io/docs/organizing/areas/) · [Entities and domains](https://www.home-assistant.io/docs/configuration/entities_domains/)
  איך מארגנים בית בפועל — ישירות רלוונטי לאופן שבו לקוחות יראו את הבית שלהם.
- [Home Assistant — Documentation index](https://www.home-assistant.io/docs/)
  אינדקס התיעוד המלא — נקודת חיפוש לכל שאלה ספציפית.
- [Home Assistant — Automation basics](https://www.home-assistant.io/docs/automation/basics/) · [State trigger](https://www.home-assistant.io/triggers/state/) · [Troubleshooting automations](https://www.home-assistant.io/docs/automation/troubleshooting/) · [Automation YAML](https://www.home-assistant.io/docs/automation/yaml/)
  המקור לשיעור 0003: שלושת החלקים, שדה For (מתאפס ב-restart), Traces (5 אחרונות), תחביר YAML נוכחי (`triggers`/`trigger:`/`action:`). הערה: דפי הטריגרים עברו ל-`/triggers/<type>/`, ו-`/docs/automation/trigger/state/` מחזיר 404.
- [Home Assistant — Person](https://www.home-assistant.io/integrations/person/) · [Zone](https://www.home-assistant.io/integrations/zone/) · [Conditions](https://www.home-assistant.io/docs/scripts/conditions/) · [Developer tools](https://www.home-assistant.io/docs/tools/dev-tools/)
  המקור לשיעור 0004: סדר העדיפויות של person בין מקורות (בבית: חיבור לפני GPS; בחוץ: GPS קודם), מצב zone הוא מספר האנשים, רדיוס ברירת מחדל 100 מטר, Set state זמני ונדרס. הערה: תנאי zone עבר לתחביר `condition: zone.in_zone` עם `target`/`options`.
- [Companion app — Location](https://companion.home-assistant.io/docs/core/location/) · [Notifications basic](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
  האפליקציה לנייד: `device_tracker`, הרשאות מיקום ברקע, תדירות עדכון (iOS: עד כ-15 דקות; Android: 1–3 דקות), והפעולה `notify.mobile_app_<device_id>`. הערה: `/docs/notifications/basic/` ו-`/docs/onboarding/` מחזירים 404.
- [Home Assistant — Using automation blueprints](https://www.home-assistant.io/docs/automation/using_blueprints/) · [Creating a blueprint](https://www.home-assistant.io/docs/blueprint/tutorial/) · [Blueprint schema](https://www.home-assistant.io/docs/blueprint/schema/)
  המקור למסלול ה-full-stack: איך בונים אוטומציה אחת פעם אחת ומשכפלים בין לקוחות — ישירות רלוונטי ל-Fleet/Ops (PRD 4) ול-golden backup template.
- [Home Assistant Developer Docs — Entities: integrating devices & services](https://developers.home-assistant.io/docs/architecture/devices-and-services/)
  להבנה עמוקה יותר של הארכיטקטורה, למסלול ה-full-stack.
- [Awesome Home Assistant (frenck/awesome-home-assistant)](https://github.com/frenck/awesome-home-assistant)
  רשימה אצורה (curated) של add-ons, dashboards, blueprints ואינטגרציות — מקום טוב לחפש פתרון לפני שבונים אחד מאפס.

## Knowledge — ספציפי ל-OneHome (כבר נחקר על ידי גיא, ב-`plan-site`)

המקורות האלה כבר מתועדים ומאומתים בעבודה הפנימית של גיא — משמשים כידע ראשוני לשיעורים על Nabu Casa, Open Home Foundation, ורשת:

- `plan-site/nabu-casa.html` — השוואת 7 השירותים של Nabu Casa Cloud, כולל מקורות ל-nabucasa.com/pricing ו-support.nabucasa.com.
- `plan-site/ohf.html` — Open Home Foundation, הפרויקטים הנלווים (ESPHome, HACS, ESP Web Tools, Improv Wi-Fi, microWakeWord ועוד), מקור: openhomefoundation.org.
- `plan-site/kb.html` — פתרון תקלות רשת אמיתיות (mDNS, AP Isolation, DHCP Reservation) שכבר עלו בעבודה.
- `plan-site/claude/golden-backup-checklist.md` — טיוטת התהליך לשכפול התקנה בין לקוחות; טעון אימות בפועל.
- `plan-site/automations.html` — קטלוג רעיונות אוטומציה, ישמש כתרגילים מעשיים במסלול ה-full-stack.

## Wisdom (Communities)

- [Home Assistant Community Forum](https://community.home-assistant.io/)
  הפורום הרשמי — הכי גבוה באמון לשאלות טכניות ספציפיות (תאימות חומרה, דיבוג אינטגרציות).
- [Home Assistant Discord](https://discord.com/invite/home-assistant)
  שרת ה-Discord הרשמי — טוב לשאלות בזמן אמת ולדופק של הקהילה.
- r/homeassistant (Reddit)
  קהילה גדולה, טובה יותר לדעות/השוואות/"מה הייתם קונים" מאשר לדיבוג טכני מדויק — להשתמש בשילוב עם הפורום הרשמי, לא במקומו.

## Gaps

- **ערוץ YouTube מומלץ עדיין לא אומת** — חיפוש ראשוני העלה כמה אתרי SEO/בלוג לא מוכרים ("wiredhaus", "tecnoyfoto" וכו') שאין להם עדיין רקורד אמון מבוסס. לא להסתמך עליהם כמקור ראשי עד שיאומתו. כדאי לבדוק את הערוץ הרשמי של Home Assistant ב-YouTube ישירות מהאתר הרשמי, ולשאול בפורום/Discord אילו יוצרים נחשבים אמינים כרגע.
- **קורס/מדריך רשמי ל-Watchman וניטור צי** — גיא בחר לבנות Watchman על בסיס Alert integration פנימי של HA ולא על תוסף HACS קיים (thewatchman). כדאי בהמשך לחפש תיעוד/דוגמאות ספציפיות ל-multi-instance monitoring (מספר בתי לקוחות), לא רק בית יחיד.
- **קהילת מתקינים/אינטגרטורים מקצועיים** — לא נמצאה עדיין קהילה ספציפית ל"מתקיני HA כעסק" (בניגוד להוביסטים). שווה לבדוק את תוכנית המתקינים של Nabu Casa שבפיתוח (ראו `decision-network-access.md`) כערוץ פוטנציאלי בעתיד.

## העדפות קהילה

טרם נשאל גיא במפורש אם הוא מעוניין להצטרף לקהילות (פורום/Discord) בשלב הזה — לשאול כשמגיעים לנושא שדורש wisdom (למשל דיבוג תאימות חומרה ספציפי).
