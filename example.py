from ast import literal_eval

import telebot

TOKEN = "734820541:AAEkVd8f-haWGhYPmiB3AHXbJtAqMOcNWqY"
bot = telebot.TeleBot(TOKEN)

white_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] + ['*', '/', '+', '-', '%']


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hello:) I can say you results of expressions.\n', parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    good = all(map(lambda x: x in white_list, text))
    print(good, text, list(map(lambda x: x in white_list, text)))
    if not good:
        print("It was not good")
        bot.send_message(chat_id, "I can't understand")
    else:
        try:
            print("I want to do it")
            result = literal_eval(text)
            bot.send_message(chat_id, text + '=' + result)
        except:
            print("I cant")
            bot.send_message(chat_id, "I can't understand")


bot.polling(none_stop=True)

