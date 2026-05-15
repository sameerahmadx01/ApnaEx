from flask import Flask
import threading
from bot import Bot   # tumhara bot module

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    # Bot ko background thread me start karo
    threading.Thread(target=run_bot).start()
    # Flask ko port 10000 pe run karo
    app.run(host="0.0.0.0", port=10000)
