from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor
import os
import asyncio
from aiohttp import web

async def handle(request):
    return web.Response(text="✅ Бот работает!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
API_TOKEN = os.getenv("BOT_TOKEN")  # получаем токен из переменной окружения

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def main():
    # стартуем HTTP-сервер
    asyncio.create_task(start_server())

    # далее твой aiogram бот
    dp = Dispatcher(...)
    await dp.start_polling(...)
@dp.message_handler(commands=['start'])
async def send_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🛡 Получить VPN",
            web_app=WebAppInfo(url="https://johnriddderrr.github.io/monetag-vpn-app/")
        )]
    ])
    await message.answer("Нажми кнопку и активируй VPN через рекламу:", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
