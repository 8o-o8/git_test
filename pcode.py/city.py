from random import choice
from telebot import TeleBot, types
TOKEN = "7770797337:AAGq_fXQ7FQfKFwZT7XDYZhcB6wSsMKH2Pw"
bot = TeleBot(TOKEN)
game = False
used_words = []
letter = ''
points = 0
with open('cities.txt', 'r', encoding='utf-8') as f:
    cities = [word.strip().lower() for word in f.readlines()]

def select_letter(text):
    i = 1
    while text[-1*i] in ('ъ', 'ы', 'й'):
        i += 1
    return text[-1*i]

@bot.message_handler(commands=['goroda'])
def start_game(message):
    global game
    global letter
    game = True
    city = choice(cities)
    letter = select_letter(city)
    bot.send_message(message.chat.id, text=city)

@bot.message_handler()
def play(message):
    global used_words, letter, game, points
    if game:
        if message.text.lower() in used_words:
            bot.send_message(message.chat.id, 'Город назывался!')
            return
        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id, 'Не та буква!')
            return
        if message.text.lower() in cities:
            letter = select_letter(message.text.lower())
            used_words.append(message.text.lower())
            for city in cities:
                if city[0] == letter and city not in used_words:
                    letter = select_letter(city)
                    bot.send_message(message.chat.id, city)
                    used_words.append(city)
                    return
            bot.send_message(message.chat.id, 'Я проиграл')
            game = False
            return
        bot.send_message(message.chat.id, 'Такого города не существует!')

if __name__ == '__main__':
    bot.polling(non_stop=True)