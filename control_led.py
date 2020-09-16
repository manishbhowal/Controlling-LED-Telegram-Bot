!pip install adafruit-io
!pip install python-telegram-bot

import os
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')

from Adafruit_IO import Client, Feed
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY )

feed = Feed(name='bot') #Naming the feed that is to be created in Adafruit

result = aio.create_feed(feed) #Creation of the feed

from Adafruit_IO import Data

from telegram.ext import Updater,CommandHandler

def on(bot,update): #Function for switching on the indicator or LED
    message = "The led is turned on "
    chat_id = update.message.chat_id
    value = Data(value=1)
    value_send = aio.create_data('bot',value)
    bot.send_message(chat_id,text = message)

def off(bot,update): #Function for switching off the indicator or LED
    message = "The led is turned off "
    chat_id = update.message.chat_id
    value = Data(value=0)
    value_send = aio.create_data('bot',value)
    bot.send_message(chat_id,text = message)

u = Updater('1191599031:AAFQRONBimnOuAHZ2U-Q8ww3kY-wsQMBl3U')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
