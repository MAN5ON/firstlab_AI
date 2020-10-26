import telebot
import re

bot = telebot.TeleBot("1208252519:AAEuzIG9GNIcmHr5S37mmtDdNftI0Ws1L0g")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    lines = 0
    pattern = r'https?:\/\/(?:[-\w]+\.)?([-\w]+\.\w+)(?:\.\w+)?\/?.*'
    domen = re.findall(pattern, message.text)
    if len(domen) != 0:
        for item in domen:
            lines += 1
            bot.reply_to(message, 'Найдено: ' + str(lines) + ')' + item + '\n')
    else:
        bot.reply_to(message, 'Ничего не найдено!')


bot.polling()
