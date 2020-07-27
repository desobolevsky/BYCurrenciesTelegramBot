import time
import telebot
import yaml
import scrap

CURRENCY_CHOOSE = False


def generate_update_message(request_type):
    """Returns a string with last time rates were updated"""
    return 'По состоянию на ' + time.strftime('%d.%m.%Y %H.%M',
                                              time.localtime(scrap.rates_data[request_type]['last_check_time']))


def get_rate_keys(message_text):
    """Returns keys for each currency for dictionary with rates.
    See scrap.scrap_bank_currencies() for better understanding"""
    if message_text.lower() == 'usd':
        rate_keys = ['USD_buy', 'USD_sell']
    elif message_text.lower() == 'eur':
        rate_keys = ['EUR_buy', 'EUR_sell']
    elif message_text.lower() == 'rub':
        rate_keys = ['100RUB_buy', '100RUB_sell']
    else:
        raise Exception
    return rate_keys


with open('config.yaml') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    API_key = config['api_key']

bot = telebot.TeleBot(API_key, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Started bot.")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Help")


@bot.message_handler(commands=['general'])
def general_currencies_message(message):
    general_rates = scrap.scrap_general_currencies()

    message_reply = '<b>Валюта</b>:   Покупка - Продажа\n\n'
    for k, v in general_rates.items():
        message_reply += ("<b>{}</b>: {} - {}\n".format(k, v[0], v[1]))

    bot.send_message(message.chat.id, message_reply)
    bot.send_message(message.chat.id, generate_update_message('general'))


# keyboard to choose rate user want to display
keyboard_choose = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_choose.row('USD', 'EUR', 'RUB')
# keyboard used to hide keyboards from user
keyboard_remove = telebot.types.ReplyKeyboardRemove(selective=False)


@bot.message_handler(commands=['banks'])
def by_bank_message(message):
    global CURRENCY_CHOOSE
    CURRENCY_CHOOSE = True
    bot.send_message(message.chat.id, 'На данный момент доступны только USD, EUR и RUB')
    bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=keyboard_choose)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global CURRENCY_CHOOSE
    if CURRENCY_CHOOSE:
        try:
            banks_rates = scrap.scrap_bank_currencies()

            rate_index = get_rate_keys(message.text)
            message_reply = '<b>Банк</b>:   Покупает - Продает\n\n'
            for rate in banks_rates:
                message_reply += (
                    '<b>{}</b>: {} - {} \n'.format(rate['bank_name'], rate[rate_index[0]], rate[rate_index[1]]))

            bot.send_message(message.chat.id, message_reply, reply_markup=keyboard_remove)
            bot.send_message(message.chat.id, generate_update_message('banks'))

            CURRENCY_CHOOSE = False
        except Exception:
            bot.send_message(message.chat.id, 'Неверная валюта, попробуйте еще раз.')
    else:
        bot.send_message(message.chat.id, 'Я Вас не понимаю :(')


bot.polling()
