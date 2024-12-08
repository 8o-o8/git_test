import json
from telebot import TeleBot, types

TOKEN = '7770797337:AAGq_fXQ7FQfKFwZT7XDYZhcB6wSsMKH2Pw'
bot = TeleBot(TOKEN)
indx = 0
points = 0

with open('my_quizz.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_next_question(data, indx):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(4):
        btn = types.KeyboardButton(data[indx]['вариант'][i])
        markup.add(btn)
    markup.add(types.KeyboardButton("Выход"))
    return markup

@bot.message_handler(commands=['points'])
def get_points(message):
    bot.send_message(message.chat.id, text=f'Набрано очков: {points}')

@bot.message_handler(commands=['quizz'])
def quizz(message):
    global game
    global indx
    game = True
    markup = get_next_question(data, indx)
    if 'image' in data[indx]:
        img = open(data[indx]['image'], 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
    bot.send_message(
        message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)

@bot.message_handler()
def vicktorinas(message):
    global game
    global indx
    global points
    if game:
        if message.text == data[indx]['ответ']:
            bot.send_message(message.chat.id, 'Правильно')
            points += 1
        elif message.text == "Выход":
            game = False
            bot.send_message(message.chat.id, 'Пока')
            return
        else:
            markup = get_next_question(data, indx)
            bot.send_message(
                message.chat.id, f'Неправильно! Прфвильный ответ - {data[indx]['ответ']}')
        indx += 1
        if len(data) < indx:
            markup = get_next_question(data, indx)
            if 'image' in data[indx]:
                img = open(data[indx]['image'], 'rb')
                bot.send_photo(message.chat.id, img)
                img.close()
            bot.send_message(message.chat.id,
                             text=data[indx]['вопрос'], reply_markup=markup)
            
if __name__ == '__main__':
    bot.polling(non_stop=True)