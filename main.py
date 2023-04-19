import telebot
import config
import socket
import stun

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])


def test1(message):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    bot.send_message(message.chat.id, IPAddr)
    print(hostname)
    print(IPAddr)


bot.polling(none_stop=True)

