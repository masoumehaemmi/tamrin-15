import random
from datetime import date , datetime
from khayyam import JalaliDate , JalaliDatetime
from gtts import gTTS
from typing import Text
import khayyam
import telebot
from telebot.types import Message
import math
mybot = telebot.TeleBot("2028397609:AAHTTHWu45NmwEX8o9dFKg1YTICcYqGIJUg")
number =random.randint(1,20)


mybutten = telebot.types.ReplyKeyboardMarkup(row_width= 1)

btn1 = telebot.types.KeyboardButton("new game")

mybutten.add(btn1)

@mybot.message_handler(commands=["start"])

def send_welcome(message):
    mybot.reply_to(message,f"Hi  {message.from_user.first_name} خوش آمدید \n /help انتخاب کن تا کمکت کنم" )


@mybot.message_handler(commands=["help"])
def help(message):
    mybot.reply_to(message ,            "کمک میخوای؟ من برای کمک به شما آماده ام \
                            \n  /game اگر دوست داری با هم بازی حدس عدد شروع کنیم \
                            \n  /age  تاریخ تولدت وارد کن تا من بگم چندسال هست داری اکسیژن مصرف می کنی  \
                            \n  /voice یه جمله به انگلیسی تایپ کن من جمله رو برات بخونم \
                            \n /qrcode مشخصات یه محصول وارد کن تا من کیو آرکدش بگم \
                            \n /max چند تا عدد وارد کن من بزرگترین عدد برات اعلام کنم \
                            \n /argmax چندتا عدد وارد کن من اندیس بزرگترین عدد نمایش بدم ")

# help(Message)

@mybot.message_handler(commands=["game"])
def game(message ):
     play= mybot.reply_to(message , "اومدیم با هم بازی حدس اعداد انجام بدیم؟ یه عددبین 1 تا 20 انتخاب کن و بزن بریم" )
     mybot.register_next_step_handler(play , new_game )
    

# @mybot.message_handler( func=lambda  message:True)
def new_game(message):
    global number
    if int(message.text) == number:
        mybot.reply_to(message ,"درست حدس زدی.آفرین")
        global game
        
    elif int(message.text ) > number:
        mybot.reply_to(message ,"برو پایین")


    elif int(message.text) < number :
        mybot.reply_to(message ,"برو بالا")

    # else: 
    #     mybot.send_message(message , " دفت کن و عدد درست انتخاب کن")

@mybot.message_handler(commands=["age"])
def enter_ege(message):
    date = mybot.reply_to(message ,"تاریخ تولدت وارد کن به صورت yyyy/mm/dd ")
    mybot.register_next_step_handler(date , Age)
    
# @mybot.message_handler(func= lambda message:True)
def Age(message):
    mybot.reply_to(JalaliDate.todate())


@mybot.message_handler(commands=["voice"])
def sentences(message):
    voice = mybot.reply_to(message,"یک جمله به لاتین وارد کن:")
    mybot.register_next_step_handler(voice ,Voice )

def Voice(message):
    mytext = message.text
    language = "en"
    my_voice = gTTS(text=mytext,lang=language ,slow=False)
    my_voice.save("voice.mp3")
  

@mybot.message_handler(commands=["qrcode"])
def Code(message):
    rcode = mybot.reply_to(message , "جمله ی خود را وارد کنید :")
    mybot.register_next_step_handler(rcode , qrcode)

def qrcode(message):
    text = message
    image = qrcode.make(text)
    image.save("qrcode.png")

@mybot.message_handler(commands=["max"])
def araye(message):
    array = mybot.reply_to(message , " چند عدد وارد کنید وبعد از هرکدام ،بگذارید.تا بزرگترین عدد اعلام کنم")
    mybot.register_next_step_handler(array , Max)

def Max(message):
    arrayeh = []
    arrayeh.append(arrayeh)
    m = max(arrayeh)
    
@mybot.message_handler(commands=["argmax"])
def arg(message):
    andis = mybot.reply_to(message , " چند عدد وارد کنید وبعد از هرکدام ، بگذارید.تا بزرگترین اندیس عدد اعلام کنم")
    mybot.register_next_step_handler(andis , Argmax)

def Argmax(message):
    argm = []
    m = max(argm[0])


mybot.polling()



