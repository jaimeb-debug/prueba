from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-lite') # Usamos 'gemini-pro' ya que 'gemini-flash-2.0-lite' no es un modelo directamente accesible a través de la API de Generative AI al momento de mi última actualización. Gemini Pro es una excelente alternativa rápida y eficiente.

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ask", methods=['POST'])
def ask():
    user_message = request.form['message']
    try:
        response = model.generate_content(user_message)
        bot_response = response.text
        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)