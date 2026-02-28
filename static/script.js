function copyText() {
  const text = document.getElementById("translatedText").innerText.trim();

  if (!text) {
    alert("No text to copy!");
    return;
  }

  navigator.clipboard.writeText(text)
    .then(() => alert("Copied successfully!"))
    .catch(err => console.error("Copy failed:", err));
}

function speakText() {
  const text = document.getElementById("translatedText").innerText.trim();

  if (!text) {
    alert("No text to speak!");
    return;
  }

  const speech = new SpeechSynthesisUtterance(text);

  const selectedLang = document.querySelector("select[name='languages']").value;
  speech.lang = selectedLang;

  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(speech);
}