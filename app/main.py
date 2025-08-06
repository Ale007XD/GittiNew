import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from dotenv import load_dotenv
from app.gemini_client import get_gemini_response
from app.history import get_history, add_message, init_db

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.startup()
async def on_startup():
    await init_db()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await add_message(message.from_user.id, message.text, "user")
    # По желанию: можно добавить авто-резюме прошлого урока через get_history и отправлять в Gemini для генерации приветствия
    prompt = "Привет! Я Гит-АИ-Ро, твой друг и наставник в мире гитары! 🎸 Готов начать?"
    await add_message(message.from_user.id, prompt, "bot")
    await message.reply(prompt)

@dp.message()
async def handle_message(message: types.Message):
    await add_message(message.from_user.id, message.text, "user")
    history = await get_history(message.from_user.id, limit=10)
    reply = await get_gemini_response(message.text, history)
    await add_message(message.from_user.id, reply, "bot")
    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

