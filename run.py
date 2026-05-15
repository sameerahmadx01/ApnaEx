# run.py
# Safe launcher for Flask + Bot

import subprocess
from multiprocessing import Process

def run_app():
    # Flask server start karega
    subprocess.run(["python", "app.py"], check=True)

def run_bot():
    # Telegram bot start karega
    subprocess.run(["python", "extractor.py"], check=True)

if __name__ == "__main__":
    app_proc = Process(target=run_app, name="web_app")
    bot_proc = Process(target=run_bot, name="telegram_bot")

    app_proc.start()
    bot_proc.start()

    app_proc.join()
    bot_proc.join()
