import operator

from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import api_key


def greet_user(bot, update):
    bot.sendMessage(update.message.chat_id,
                    # reply_markup=reply_markup,
                    text="Список доступных команд:\n"
                         "Калькулятор, пример: 33*44 \n"
                         "Счетчик количества слов /wordcount слова количество которых будет посчитано\n"
                    )


def word_counter(bot, update):
    print("Вызван /wordcount")
    amount_of_words = len(update.message.text.split()) - 1
    if amount_of_words > 0:
        bot.sendMessage(update.message.chat_id, text=amount_of_words)


def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))


def calculator(bot, update):

    keyboard = [[KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3'), KeyboardButton('*')],
                [KeyboardButton('4'), KeyboardButton('5'), KeyboardButton('6'), KeyboardButton('÷')],
                [KeyboardButton('7'), KeyboardButton('8'), KeyboardButton('9'), KeyboardButton('+')],
                [KeyboardButton('='), KeyboardButton('0'), KeyboardButton('.'), KeyboardButton('-')]
                ]
    reply_markup = ReplyKeyboardMarkup(keyboard)

    available_signs = '+-:/*'
    operations_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        ':': operator.truediv,
        '/': operator.truediv,
    }

    data_from_user = update.message.text
    operation_sign = None

    for sing in available_signs:
        if sing in data_from_user:
            operation_sign = sing
            break

    if operation_sign is None:
        bot.sendMessage(update.message.chat_id, text='Непонятное действие, я умею только такие: +-:*', reply_markup=reply_markup)
    elif operation_sign == ':' or operation_sign == '/' and data_from_user[-1] == '0':
        bot.sendMessage(update.message.chat_id, text='Не умею делить на ноль.', reply_markup=reply_markup)
    else:
        data = data_from_user.split(operation_sign)
        result = operations_dict[operation_sign](int(data[0]), int(data[1]))
        bot.sendMessage(update.message.chat_id, text=result, reply_markup=reply_markup)

    # operation_sign = get_operation_sign(data_from_user)
    # operands = get_operands(data_from_user, operation_sign)
    # operation_result = apply_operation(operation_sign, operands)
    # send_reply(operation_result)


def main():
    updater = Updater(api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], calculator))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
