import telebot
import yaml

with open('config.yaml') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    API_key = config['api_key']

bot = telebot.TeleBot(API_key)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Started bot.")


bot.polling()
