import telebot
import config
import socket
import urllib
import bs4
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])


def test1(message):
    page = urllib.urlopen('https://2ip.ru/')
    soup = BeautifulSoup(page)

    x = soup.body.find('span', attrs={'class': 'ip'}).text

    print(x)
    hostname = socket.gethostname()

    IPAddr = socket.gethostbyname(hostname)
    bot.send_message(message.chat.id, IPAddr)
    print(IPAddr)
    print(soup.ip)


bot.polling(none_stop=True)

