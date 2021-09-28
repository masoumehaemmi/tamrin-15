import random
from datetime import date , datetime
from khayyam import JalaliDate , JalaliDatetime
from gtts import gTTS
from typing import Text
import khayyam
import telebot
from telebot.types import Message

mybot = telebot.TeleBot("2028397609:AAHTTHWu45NmwEX8o9dFKg1YTICcYqGIJUg")
number =random.randint(0,20)
mymarkup = telebot.types.ReplyKeyboardMarkup(row_width=3)

mybutten = telebot.types.ReplyKeyboardMarkup(row_width= 1)
btn1 =  telebot.types.KeyboardButton("muzic")
btn2 = telebot.types.KeyboardButton("video")
btn3 = telebot.types.KeyboardButton("pic")

mymarkup.add(btn1,btn2,btn3)
btn4 = telebot.types.KeyboardButton("new game")
mybutten.add(btn4)

@mybot.message_handler(commands=["start"])

def send_welcome(message):
    mybot.reply_to(message,f"Hi  {message.from_user.first_name}")

@mybot.message_handler(commands=["game"])
def new_game(message ):
    # mybot.reply_to(message , "agar mikhai bazi jadid aghaz koni dokme new game bezan", REPLY_MARKUP_TYPES = mybutten )
    number =random.randint(0,20)
# @mybot.message_handler(commands=["Game"])

@mybot.message_handler( func=lambda  message:True)
def new_game(message):
    global number
    if int(message.text) == number:
        mybot.reply_to(message ,"dorost hads zadi")
        global new_game
        
    elif int(message.text ) > number:
        mybot.reply_to(message ,"boro paeen")


    elif int(message.text) < number :
        mybot.reply_to(message ,"boro bala")

@mybot.message_handler("age")
def enter_ege(message):
    mybot.reply_to(message ,"enter your date birthday (yyyy / mm / dd): ")

    
@mybot.message_handler(func= lambda message:True)
def Age(message):
    print(JalaliDate.message.todate())


@mybot.message_handler("voice")
def sentences(message):
    mybot.reply_to(message,"enter your sentences:")

mybot.message_handler(func= lambda message:True)
def voice(message):
    mytext = message
    language = "en"
    myobj = gTTS(text=mytext,lang=language ,slow=False)
    myobj.save("voice.mp3")


@mybot.message_handler(commands=["download"])
def my_down(message):
    mybot.reply_to(message, "kodom mikhay dhnlod koni", reply_markup =mymarkup )

@mybot.message_handler(commands=["help", "komak"])
def my_function_1(message):
    mybot.reply_to(message, "کمک میخوای؟ من اینجا برای خدمت گزاری آماده ام")

@mybot.message_handler(commands=["fal"])
def send_fal(message):
    falha = ["به سفر خواهی رفت","به دیدار معشوق خواهی رفت", "به فناخواهی رفت"]
    selected_fal= random.choice(falha)
    mybot.reply_to(message , selected_fal)

@mybot.message_handler(func=lambda message:True)
def my_function_3(message):
    if message.text == "salam":
        mybot.reply_to(message ,"hello")
    elif message.text == "fine?":
        mybot.reply_to(message , "چطوری ؟")
    elif message.text == "bos":
        mybot.reply_to(message ,"boss")
    elif message.text =="chi poshidi":
        photo = open("saeidhe.jpg", "rb")
        mybot.send_photo(message.chat.id, photo)

    else:
        # mybot.reply_to(message,"nemifahmam chi migi")
        mybot.send_message(message.chat.id,"nemifahmam chi migi")


mybot.polling()



