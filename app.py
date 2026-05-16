from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Extractor bot is running!"

def run_bot():
    os.system("python -m Extractor")

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
