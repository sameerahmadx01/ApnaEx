from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    with open("log.txt", "a") as f:
        f.write(f"Start command from {message.from_user.id}\n")
    await message.reply_text("Bot is working ✅")
