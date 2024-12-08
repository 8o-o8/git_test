from telebot import TeleBot

Token = '7672250382:AAFbmxf2AD74duJFpUJ5dXO29uP87BNGg8k'
bot = TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    img = open('taxi.png', 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.send_message(message.chat.id, 'Приветствуем на нашей компании такси мы одна из больших компаний по такси в мире и имя ей "Sav-Taxi" мы рады что вы посетили нашего бота таксиста!\nНам бы узнать чтобы вы хотели расскажите пожалуйста:\nт\Такси\nДоставка\nГрузовой')

if __name__ == '__main__':
    bot.polling(none_stop=True)