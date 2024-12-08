import requests
from telebot import TeleBot, types
import wikipedia

TOKEN = '7770797337:AAGq_fXQ7FQfKFwZT7XDYZhcB6wSsMKH2Pw'
bot = TeleBot(TOKEN)


def random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']



def random_fox():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

wikipedia.set_lang('ru')


@bot.callback_query_handler(func=lambda call: call.data)
def answer(call):
    page = wikipedia.page(call.data)
    bot.send_message(call.message.chat.id, text=page.title)
    bot.send_message(call.message.chat.id, text=page.summary)
    bot.send_message(call.message.chat.id, text=page.url)



@bot.message_handler(commands=['wiki'])
def wiki(message):
    text = ' '.join(message.text.split(' ')[1:])
    results = wikipedia.search(text)
    markup = types.InlineKeyboardMarkup()
    for res in results:
        markup.add(types.InlineKeyboardButton(res, callback_data=res))
    bot.send_message(
        message.chat.id, text='Смотри что я нашел!', reply_markup=markup)


@bot.message_handler(commands=['duck'])
def duck(message):
    url = random_duck()
    bot.send_message(message.chat.id, url)

@bot.message_handler(commands=['fox'])
def fox(message):
    url = random_fox()
    bot.send_message(message.chat.id, url)


if __name__ == '__main__':
    bot.polling(none_stop=True)