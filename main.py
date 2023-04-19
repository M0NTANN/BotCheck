import telebot
import config
import http.client
import threading
import checkPC
import  time
from pythonping import ping


bot = telebot.TeleBot(config.TOKEN)

listCommand = ['/help - список имеющихся команд', '/ip - ip компьютера', '/check - проверить адресс']
listID = ['739252019']
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

@bot.message_handler(commands=['check'])
def checkCon(message):
    id = message.chat.id
    xx = str(id)
    t = threading.Thread(target=checkPC.work)
    t.start()

bot.polling(none_stop=True)

def work():
    yes = "work"
    no = "no work"
    address = "192.168.2.89"
    loopstatus = False
    while loopstatus == False:
        x = ping(address, verbose=False, timeout=0, count=1)
        if (x == 2):
            bot.send_message(listID[0], address + " work")
        else:
            bot.send_message(listID[0], address + " no work")
        time.sleep(5)
