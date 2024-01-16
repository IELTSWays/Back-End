from telegram import Bot
from config.exceptions import CustomException


async def send_telegram_message(phone_number, message):
    try:
        bot = Bot(token='6589901044:AAFl2ct4kggaT-rZR0rtEkfAKJ6VS1OvZuk')
        await bot.send_message(chat_id=phone_number, text=message)
    except CustomException as e:
        print(e.detail)
