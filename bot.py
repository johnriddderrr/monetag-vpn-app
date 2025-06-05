from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # получаем токен из переменной окружения

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

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
