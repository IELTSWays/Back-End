from telegram.ext import Updater, CommandHandler
from telegram import Bot
from config.exceptions import CustomException



def send_tele_otp():
    bot = Bot(token="6589901044:AAFl2ct4kggaT-rZR0rtEkfAKJ6VS1OvZuk")
    print('--')
    try:
        bot.send_message(chat_id='nimadorostkar', text='Hello Nima from Django!')
    except CustomException as e:
        print('-----------')
        print(e)



