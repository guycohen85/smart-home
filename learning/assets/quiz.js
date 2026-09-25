// OneHome Learning Workspace — Quiz widget (shared component)
// שימוש: <div class="quiz"><p class="quiz-q">...</p><button class="quiz-reveal-btn" onclick="revealQuiz(this)">הצג תשובה</button><p class="quiz-answer">...</p></div>
function revealQuiz(btn) {
  var answer = btn.nextElementSibling;
  if (!answer) return;
  var shown = answer.classList.toggle('shown');
  btn.textContent = shown ? 'הסתר תשובה' : 'הצג תשובה';
}
