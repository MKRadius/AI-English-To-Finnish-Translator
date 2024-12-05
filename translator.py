from flask import Flask, render_template, request, jsonify
from transformers import pipeline

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') 

@app.route('/translate', methods=['POST'])
def sendStringToBeTranslated():
    user_input = request.json.get('text', '')
    result = pipe(user_input)
    return jsonify({'result': result[0]['translation_text']})

if __name__ == '__main__':
    app.run()