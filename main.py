import telebot
import config
import http.client

bot = telebot.TeleBot(config.TOKEN)

listCommand = ['/help - список имеющихся команд', '/ip - ip компьютера']
@bot.message_handler(commands=['ip'])
def checkip(message):
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    x = conn.getresponse().read()
    bot.send_message(message.chat.id, x)

@bot.message_handler(commands=['help'])
def help(message):
    for(index, elem) in enumerate(listCommand):
        bot.send_message(message.chat.id, listCommand[index])

bot.polling(none_stop=True)

