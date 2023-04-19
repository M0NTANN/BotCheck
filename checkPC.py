import telebot
import config
import http.client
import threading
import time
from pythonping import ping

bot = telebot.TeleBot(config.TOKEN)
def work():
    yes = "work"
    no = "no work"
    address = "192.168.2.89"
    loopstatus = False
    while loopstatus == False:
        x = ping(address, verbose=False, timeout=0, count=1)
        if (x == 2):
            bot.send_message(739252019, address + " work")
        else:
            bot.send_message(739252019, address + " no work")
        time.sleep(2)