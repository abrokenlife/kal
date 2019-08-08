from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import sys

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO,
            filename='bot.log'
            )

def piska(bot, update):
    handle = open("text.txt", 'r')
    names = handle.read()
    name_list = []
    name = ''

    for i in names:
        if i == '\n':
            name_list.append(name)
            name = ''
        elif i == names[-1]:
            name += i
            name_list.append(name)
            name = ''
        elif i != '':
            name += i

    for i in name_list:
        if i == '':
            name_list.remove(i)
    name = update.message.from_user.first_name
    text = ' писю соси'
    update.message.reply_text(name + text)
    print(name_list)

    for i in name_list:

        if (name + " ") == i:
            continue
        else:
            text1 = ' и ты писю соси'
            update.message.reply_text(i + text1)

def start(bot, update):
    name = update.message.from_user.first_name
    handle = open("text.txt", 'r')
    name_list = handle.read()
    skl = open("text.txt", 'a')
    if name not in name_list:
        skl.write('\n' + name + ' ')

def clear(bot, update):
    file = open('text.txt', 'w')
    file.write('')

def message(bot, update):
    user_message = update.message.text
    print(user_message)

    if (user_message.lower() == 'петя лох?') or \
            (user_message.lower() == 'петя лох'):
        update.message.reply_text('Да')
    else:
        update.message.reply_text("Нет")

def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('piska', piska))
    dp.add_handler(CommandHandler('clear', clear))
    dp.add_handler(MessageHandler(Filters.text, message))

    mybot.start_polling()
    mybot.idle()

print(sys.path)

main()

