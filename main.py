import telebot
import config
import socket

import http.client

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])


def test1(message):
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    x = conn.getresponse().read()
    print(x)
    hostname = socket.gethostname()

    IPAddr = socket.gethostbyname(hostname)
    bot.send_message(message.chat.id, x)
    print(IPAddr)


bot.polling(none_stop=True)

