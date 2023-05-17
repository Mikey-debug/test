from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio 

API_ID = 6133145
API_HASH = "30d4307da4885a00c58089d5f5503b5b"
BOT_TOKEN = "5619875667:AAGCK37OkBEvXVXnGf696ddufCycWOvP6AE"
group = -1001728546352
channel = -1001962326301

bot = Client(
    "aa",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@bot.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)


app.run()  # Automatically start() and idle()
