import telebot
import button
import datetime
from test import *

now = datetime.datetime.now()
TOKEN = "1452055338:AAEnZSyZqQuAT2ekDbvPx-DyO3BYKiJSFLw"
bot = telebot.TeleBot(TOKEN)
#.............
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id,'Привет :)',reply_markup=button.statistics())
    #сообщение для кнопки "статистика"


@bot.message_handler(content_types= 'text' )
def process_step(message):
    # + '\nInstagram: ' + inst()
    mess = '\nНа ' + now.strftime("%d-%m-%Y %H:%M") + '\nFacebook: ' + fcbook()#'\nInstagram: ' + inst()
    if message.text=='📊 Статистика':
        #msg = bot.reply_to(message, mess)
        vk()
        print('do func')
        vk_file='vk.html'
        print('posle func')

        bot.send_document(message, vk_file)
bot.polling()