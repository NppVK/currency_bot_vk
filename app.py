import telebot
from telebot import types
from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Инструкция', callback_data='question')

    markup.add(item)

    bot.send_message(message.chat.id,
                     'Доброго времени суток, {0.first_name}!\
                     \n\nПеред началом работы, пожалуйста, ознакомтесь с инструкцией'
                     .format(message.from_user), reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'question':
            text = ("Чтобы начать работу введите команду боту в нужном формате через пробел: \
            \n<имя валюты, цену которой хотим узнать> \
            \n<имя валюты, в которой надо узнать цену перевой валюты> \
            \n<количество первой валюты> \
            \n\n Увидеть список всех доступных валют: \
            \n/values")
            bot.send_message(call.message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Достуные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров!')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
