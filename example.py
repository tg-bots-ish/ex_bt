from ast import literal_eval

import telebot

TOKEN = "734820541:AAEkVd8f-haWGhYPmiB3AHXbJtAqMOcNWqY"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hello:) I can say you results of expressions.\n', parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    try:
        print("I want to do it")
        result = literal_eval(text)
        bot.send_message(chat_id, text + '=' + result)
    except:
        print("I cant")
        bot.send_message(chat_id, "I can't understand")


bot.polling(none_stop=True)

