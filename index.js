function doTranslate()
{
    const inputLanguage = document.getElementById("fromLanguage").value;
    const outputLanguage = document.getElementById("toLanguage").value;
    const inputText = document.getElementById("fromLanguageText").value;

    if (!inputLanguage || !outputLanguage || inputText.trim() === "") {
        alert("Please fill in all fields!");
        return;
    }

    fetch('http://127.0.0.1:5000/translate', 
    {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: inputText, src: inputLanguage, dest: outputLanguage})
    })

    .then(response => 
    {
        if (!response.ok)
            throw new Error("Server error");
        return response.json();
    })
    .then(data => document.getElementById("toLanguageText").value = data.translated_text)
    .catch(error => alert("Translation failed. ", error.message));
}