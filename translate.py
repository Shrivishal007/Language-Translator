from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator

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

        translator = GoogleTranslator(source=src, target=dest)
        translated_text = translator.translate(text)
        print("Translated:", translated_text)

        return jsonify({"translated_text": translated_text})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)