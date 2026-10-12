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
- [Companion app — Actionable notifications](https://companion.home-assistant.io/docs/notifications/actionable-notifications/) · [Script syntax — wait_for_trigger / wait variable](https://www.home-assistant.io/docs/scripts/#wait-for-a-trigger)
  המקור לשיעור 0005: האירוע `mobile_app_notification_action`, מזהים ייחודיים עם `context.id`, עד 3 כפתורים באנדרואיד (כ-10 באייפון), ו-`wait.trigger` הוא `none` אחרי timeout. הערה: הדוגמאות בתיעוד האפליקציה עדיין בתחביר הישן `platform: event`, ובתחביר הנוכחי זה `trigger: event`.
- [Home Assistant — Scripts](https://www.home-assistant.io/integrations/script/) · [Script syntax — stop / response_variable](https://www.home-assistant.io/docs/scripts/#stop) · [Scenes](https://www.home-assistant.io/integrations/scene/) · [Scene editor](https://www.home-assistant.io/docs/scene/editor/)
  המקור לשיעור 0006: fields (name/description/required/default/selector/example), modes (ברירת מחדל `single`), החזרת תשובה עם `stop` + `response_variable` (חייב להיות מבנה של מפתח וערך), וקריאה ישירה מחכה לסקריפט בעוד ש-`script.turn_on` לא מחכה. סצנות: אין מצב on/off, העורך מחיל מצבים בזמן עריכה ומחזיר אותם ביציאה, `scene.create` זמני ונמחק ב-reload.
- [Home Assistant — Sections view](https://www.home-assistant.io/dashboards/sections/) · [Tile card](https://www.home-assistant.io/dashboards/tile/) · [Card actions](https://www.home-assistant.io/dashboards/actions/) · [Dashboards](https://www.home-assistant.io/dashboards/dashboards/) · [Cards: visibility](https://www.home-assistant.io/dashboards/cards/#showing-or-hiding-a-card-or-badge-conditionally) · [Person: adding a user](https://www.home-assistant.io/integrations/person/#adding-a-person-to-home-assistant)
  המקור לשיעור 0007: Sections היא תצוגת ברירת המחדל, ב-Tile הגוף פותח more-info והאייקון עושה toggle, `perform-action` עם `confirmation`, לא עורכים את Overview (דשבורד חדש לא מתעדכן לבד), Visibility של תצוגה הוא רק תצוגה (הכתובת נגישה), ומשתמש אחד עם שני דשבורדי ברירת מחדל בשני מכשירים חוזר לברירת המחדל. הערה: ב-08/10/2026 האתר home-assistant.io היה חסום מהסביבה, והתוכן נקרא מקוד המקור של התיעוד ב-`raw.githubusercontent.com/home-assistant/home-assistant.io/current/source/` (למשל `_dashboards/tile.markdown`, `dashboards/actions.markdown`). בהמשך אותו יום גיא פתח את הגישה לאתר, וברירות המחדל של Tile אומתו גם מול האתר החי.
- [Home Assistant — Apps](https://www.home-assistant.io/apps/) · [Common tasks: HA OS](https://www.home-assistant.io/common-tasks/os/) · [Glossary: App, Custom integration](https://www.home-assistant.io/docs/glossary/)
  המקור לשיעור 0008: Add-ons נקראים היום **Apps** (תפריט Settings → Apps), והם קיימים רק ב-HA OS. App היא "חבילת תוכנה עצמאית", ואת רובן מחברים ל-HA דרך אינטגרציה. מאגר צד שלישי מגיע "בלי ערובה לאיכות או לאבטחה". ב-File editor יש אפשרות Enforce basepath, ו-Studio Code Server תומך רק ב-AMD64 וב-ARM64. Custom integration "לא נבדקת על ידי צוות HA ועלולה לפגוע ביציבות". סקריפטים וסצנות מהעורך נשמרים ב-`scripts.yaml` וב-`scenes.yaml`.
- [HACS — User documentation](https://www.hacs.xyz/docs/use/) · [Prerequisites](https://www.hacs.xyz/docs/use/download/prerequisites/) · [Download](https://www.hacs.xyz/docs/use/download/download/) · [Initial configuration](https://www.hacs.xyz/docs/use/configuration/basic/)
  המקור לשיעור 0008: HACS הוא אינטגרציה מותאמת ולא App. ב-HA OS מורידים אותו דרך המאגר `https://github.com/hacs/addons` והאפליקציה Get HACS. הדרישות: HA 2024.4.1 ומעלה, גישה ל-GitHub ול-Cloudflare, חשבון GitHub עם device code, וניקוי מטמון של הדפדפן לפני הוספת האינטגרציה. "אם אתה לא יודע מה סוג ההתקנה, אל תשתמש ב-HACS".
- [Home Assistant — Assist](https://www.home-assistant.io/voice_control/) · [Exposing entities](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/) · [Aliases](https://www.home-assistant.io/voice_control/aliases/) · [Local pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/) · [Cloud pipeline](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/) · [Conversation: sentence triggers](https://www.home-assistant.io/integrations/conversation/) · [Respond to a conversation](https://www.home-assistant.io/docs/scripts/#respond-to-a-conversation)
  המקור לשיעור 0009: החשיפה ל-Assist היא בחירה לכל מכשיר, כדי למנוע הפעלה בטעות של מנעולים ושערים. Assist מזהה שמות וכינויים. Speech-to-Phrase מהיר על HA Green, ו-Whisper לוקח כ-8 שניות על Pi 4. עם ענן, "רק האודיו נשלח", והשליטה נשארת מקומית. בטריגר משפט, `()` לחלופות ו-`[]` למילים שלא חובה, ופיסוק לא משנה. `set_conversation_response` עובד רק באוטומציה. בלשונית Developer tools → Assist בודקים התאמה בלי להפעיל.
- [OHF-Voice/intents — משפטים בעברית](https://github.com/OHF-Voice/intents/tree/main/sentences/he) · [דוח כיסוי לפי שפה](https://ohf-voice.github.io/intents/) · [Speech-to-Phrase](https://github.com/OHF-Voice/speech-to-phrase) · [Piper voices](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md) · [hass-nabucasa voice.py](https://github.com/NabuCasa/hass-nabucasa/blob/main/hass_nabucasa/voice.py)
  המקור למצב העברית (נבדק 11/10/2026): בעברית יש 22 intents, כל החובה מכוסה (6/6), אבל רק 26% מכל הצירופים. התבנית `[ה]{name}` בולעת את ה"א הידיעה. ב-Speech-to-Phrase אין עברית (21 שפות), ב-Piper אין קול עברי. ב-Nabu Casa יש STT `he-IL` ושני קולות TTS (Hila, Avri). הערה: הכתובת `home-assistant.github.io/intents` מחזירה 404, והמאגר עבר ל-`OHF-Voice`.
- [Home Assistant — Installation: Windows](https://www.home-assistant.io/installation/windows) · [macOS](https://www.home-assistant.io/installation/macos) · [Onboarding](https://www.home-assistant.io/getting-started/onboarding/) · [Backups (Common tasks: general)](https://www.home-assistant.io/common-tasks/general/)
  המקור לשיעור 0010 (נבדק 11/10/2026, HA OS 18.3): ב-VirtualBox צריך לפחות 2 GB ו-2 מעבדים, EFI חובה ("requires UEFI to boot"), ורשת Bridged. ל-Mac עם מעבד Apple יש קובץ `haos_generic-aarch64` ובקר VirtioSCSI. Hyper-V בלי USB. בהגדרה הראשונית HA מוריד כ-700 MB, ואת סיסמת המשתמש הראשון אי אפשר לשחזר. גיבוי מלא כולל `config`, `share`, `addons`, `ssl` ו-`media`, הוא מוצפן, וצריך את ה-Emergency kit כדי לשחזר. בשחזור מתחברים עם המשתמש והסיסמה שהיו בזמן הגיבוי, למכשיר היעד צריך יותר מקום פנוי מאשר למקור, ובהתקנה גדולה זה כ-45 דקות. הדף לא מזכיר מגבלת גרסה בשחזור. הערה: שינוי hostname לא מתועד בדפים האלה. לפי [הפורום](https://community.home-assistant.io/t/change-ha-server-name/551486), השדה נמצא ב-Settings → System → Network.
- [Home Assistant — Using automation blueprints](https://www.home-assistant.io/docs/automation/using_blueprints/) · [Creating a blueprint](https://www.home-assistant.io/docs/blueprint/tutorial/) · [Blueprint schema](https://www.home-assistant.io/docs/blueprint/schema/)
  המקור לשיעור 0011 (נבדק 12/10/2026): קובץ Blueprint הוא אוטומציה עם `!input`, בתיקייה `blueprints/automation/` (מותר לפתוח תת-תיקיות). חובה רק `name` ו-`domain`. אוטומציה שנוצרת ממנו שומרת רק `use_blueprint` עם `path` ו-`input`, ומקבלת תיקונים לקובץ בטעינה הבאה. `!input` לא זמין בטמפלט, וצריך לעבור דרך `variables`. Take control חד-כיווני, ו-Re-import דורס את הקובץ. בורר `duration` מחזיר מבנה של שעות ודקות. סינון לפי integration לא אמין ב-Zigbee וב-Matter. מקטעי input דורשים 2024.6.0. הערה: לפי הדף, טעינת YAML עברה ל-Settings → Tools → YAML. הדפים נקראו מקוד המקור ב-`raw.githubusercontent.com/home-assistant/home-assistant.io/current/source/_docs/blueprint/`.
- [mobile_app — device_action.py (קוד הרכיב)](https://github.com/home-assistant/core/blob/dev/homeassistant/components/mobile_app/device_action.py)
  המקור לשליחת התראה לפי מכשיר בשיעור 0011: פעולת מכשיר `type: notify` מקבלת `message`, `title` ו-`data` (כולל כפתורים), ומוצאת לבד את שירות ה-notify של הטלפון. זה מה שמאפשר לבחור טלפון בטופס של Blueprint.
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
