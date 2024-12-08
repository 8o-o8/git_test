from telebot import TeleBot
from random import choice

TOKEN = '7770797337:AAGq_fXQ7FQfKFwZT7XDYZhcB6wSsMKH2Pw'
bot = TeleBot(TOKEN)



jokes = [
    '- Леночка, ты знаешь, что в одиночестве пьют только алкоголики?\n- Я не в одиночестве! Я в сети! Со мной бухает весь мир!',
    'Сервис Т9 присоседился к сенсациям противень России',
    'В советское время оформить подписку было так же сложно, как в нынешнее - от нее отказаться.'
]

#@bot.message_handler(commands=['start'])
#def start(message):
    #bot.send_message(message.chat.id, 'Добро пожаловать на бота для практики!\nНа данный момент бот имеет несколько функций такие как:\n*Пошути\n*/sum-посчитать(сложение) больше о "sum" в функции "/sum?" :)')
@bot.message_handler(commands=["start"])
def pictur(message):
    img = open('game.png', 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, 'Приветствую на игре камень ножницы бумага')
    img.close()

@bot.message_handler(commands=['sum'])
def start(message):
    val = message.text.split(' ')
    number = int(val[1]) + int(val[2])
    bot.send_message(message.chat.id, number)
@bot.message_handler(commands=['sum?'])
def start(message):
    bot.send_message(message.chat.id, 'Чтобы сложить вот вам пример "/sum чис. чис."')


@bot.message_handler()
def start(message):
    if message.text == 'Пошути':
        bot.send_message(message.chat.id, choice(jokes))
        return
    else:
        bot.send_message(message.chat.id, 'Error')
        return
    bot.send_message(message.chat.id, message.text)



game_choice = ["камень", "ножницы", "бумага"]
bot_points = 0
user_points = 0

@bot.message_handler(func=lambda x: x.text.lower() in game_choice)
def game(message):
    global bot_points
    global user_points
    user_choice = message.text.lower()
    bot_choice = choice(game_choice)
    bot.send_message(message.chat.id, bot_choice)
    if user_choice == "камень" and bot_choice == "ножницы":
        msg = 'Победа'
        user_points += 1
    elif user_choice == "ножницы" and bot_choice == "бумага":
        msg = 'Победа'
        user_points += 1
    elif user_choice == "бумага" and bot_choice == "камень":
        msg = 'Победа'
        user_points += 1
    elif user_choice == bot_choice:
        msg = 'Ничья'
    else:
        msg = 'Проигрш'
        bot_points += 1
    bot.send_message(message.chat.id, msg)
    

@bot.message_handler(commands=['points'])
def points(message):
    bot.send_message(message.chat.id, f"бот: {bot_points} игрок: {user_points}")

@bot.message_handler(commands=['reset'])
def reset(message):
    global user_points
    global bot_points
    user_points = 0
    bot_points = 0


if __name__ == '__main__':
    bot.polling(none_stop=True)