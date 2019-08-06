from telegram.ext import Updater, CommandHandler
import logging


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
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

    for i in name_list:

        if name == i:
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
        skl.write(name)

def clear(bot, update):
    f = open('text.txt', 'w')






def main():
    mybot = Updater('632006628:AAG9wyctEzEAF25XbNUDPUaNJ87UYxlXris', request_kwargs = PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('piska', piska))
    dp.add_handler(CommandHandler('clear', clear))



    mybot.start_polling()
    mybot.idle()

main()