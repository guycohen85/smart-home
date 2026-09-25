// OneHome Learning Workspace — Sort widget (shared component)
// תרגיל מיון עם משוב מיידי: לכל פריט בוחרים קטגוריה, והתשובה נבדקת מיד.
// שימוש:
// <div class="sort" data-answer="trigger" data-why="הסבר שמופיע אחרי הבחירה">
//   <p class="sort-q">טקסט הפריט</p>
//   <div class="sort-opts">
//     <button data-v="trigger">טריגר</button><button data-v="condition">תנאי</button><button data-v="action">פעולה</button>
//   </div>
//   <p class="sort-fb"></p>
// </div>
document.addEventListener('click', function (e) {
  var btn = e.target.closest('.sort-opts button');
  if (!btn) return;
  var item = btn.closest('.sort');
  if (item.classList.contains('done')) return;
  var fb = item.querySelector('.sort-fb');
  var why = item.getAttribute('data-why') || '';
  if (btn.getAttribute('data-v') === item.getAttribute('data-answer')) {
    btn.classList.add('right');
    item.classList.add('done');
    fb.textContent = '✓ נכון. ' + why;
    fb.className = 'sort-fb shown right';
  } else {
    btn.classList.add('wrong');
    btn.disabled = true;
    fb.textContent = '✗ לא זה. נסה שוב.';
    fb.className = 'sort-fb shown wrong';
  }
  updateSortScore();
});

function updateSortScore() {
  var el = document.querySelector('.sort-score');
  if (!el) return;
  var all = document.querySelectorAll('.sort');
  var firstTry = 0, done = 0;
  all.forEach(function (s) {
    if (s.classList.contains('done')) {
      done++;
      if (!s.querySelector('button.wrong')) firstTry++;
    }
  });
  el.textContent = done + ' מתוך ' + all.length + ' מוינו · ' + firstTry + ' נכונים בניסיון ראשון';
}
document.addEventListener('DOMContentLoaded', updateSortScore);
