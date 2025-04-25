import telebot, json, requests
from telebot import types

token = "7828368741:AAFDGiDZepcvlxgKyxF5Cy7GeeYp723Qb_Y"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("Получить информацию")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}! Я бот для получение картинки и информации о котах и собаках".format(message.from_user), reply_markup=markup)
def get_cat_url():
    response_cat = requests.get('https://api.thecatapi.com/v1/images/search').text
    return json.loads(response_cat)[0]['url']

def get_dog_url():
    response_dog = requests.get('https://api.thedogapi.com/v1/images/search').text
    return json.loads(response_dog)[0]['url']

@bot.message_handler(commands=['info_about_us'])
def func(message):
    bot.send_message(message.chat.id, text=(f"Студенты группы №643\nМаментьев Кирилл,@mamento355\nКурденевич Влад,@MORKOVKa_228z\nДеньги кидать сюда 5536 9141 7510 0571"))

@bot.message_handler(commands=['other_bots'])
def func(message):
    bot.send_message(message.chat.id, text=(f"Бот,который показывает погоду: @dvasg_bot"))

@bot.message_handler(commands=['info_about_the_bot'])
def func(message):
    bot.send_message(message.chat.id, text=(f"Команды которые есть в боте. otherbots,info"))


@bot.message_handler()
def dif(message):
    if (message.text == "Привет"):
        bot.send_message(message.chat.id, text="Привеет!)")
    if (message.text == "Получить информацию"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn21 = types.KeyboardButton("Кошка")
        btn32 = types.KeyboardButton("Собака")
        markup.add(btn21, btn32)
        bot.send_message(message.chat.id, text="О ком хотите получить информацию и картинку?\n Собака или Кошка", reply_markup=markup)
    elif (message.text == "Кошка"):
        picture = get_cat_url()
        bot.send_photo(message.chat.id, picture)
        bot.send_message(message.chat.id,text="Кошка - домашнее животное, которое наряду с собакой считается «животным-компаньоном». Согласно данным генетических исследований, все домашние кошки происходят от представительниц подвида дикая ближневосточная (ливийская) кошка (лат. Felis silvestris lybica) — мелкого хищного млекопитающего семейства кошачьих. Одомашнивание кошки произошло примерно 9500 лет назад на Ближнем Востоке в районе Плодородного полумесяца, где зародились и располагались древнейшие человеческие цивилизации")
    elif message.text == "Собака":
        picture = get_dog_url()
        bot.send_photo(message.chat.id, picture)
        bot.send_message(message.chat.id,text="Собака - плацентарное млекопитающее отряда хищных семейства псовых. В настоящее время имеются сотни пород собак, которые значительно отличаются друг от друга и внешностью, и характером. Например, высота в холке может варьировать от нескольких сантиметров (чихуахуа) до почти метра (ирландский волкодав, дог), цвет — от белого до чёрного, включая рыжий, серый, коричневый, в большом разнообразии оттенков.")
bot.infinity_polling()