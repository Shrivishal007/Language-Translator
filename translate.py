from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])

def translate():
    try:
        data = request.json
        print("Received:", data)

        text = data.get('text')
        src = data.get('src')
        dest = data.get('dest')
        
        if not text or not src or not dest:
            return jsonify({"error": "Missing data"}), 400

        translator = Translator()
        translated = translator.translate(text, src=src, dest=dest)
        print("Translated:", translated.text)

        return jsonify({"translated_text": translated.text})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)