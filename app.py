from flask import Flask, request, jsonify
from translate_text import translate_text
import os

app = Flask(__name__)

@app.route("/translate-text", methods=["POST"])
def translate_text_route():
    try:
        # Get the text input from the request JSON
        data = request.get_json()
        input_text = data.get("text")
        target_language=data.get("lang")

        if input_text:
            # Perform translation using your function and pass the input text
            translated_text = translate_text(input_text,target_language)  # Call the translation function
        
            # Return the translated text as a JSON response
            return jsonify({"translated_text": translated_text})
        else:
            return jsonify({"error": "No text provided."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
