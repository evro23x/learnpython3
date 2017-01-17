import operator
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


def talk_to_me(bot, update):
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
        bot.sendMessage(update.message.chat_id, text='Непонятное действие, я умею только такие: +-:*')
    elif operation_sign == ':' or operation_sign == '/' and data_from_user[-1] == '0':
        bot.sendMessage(update.message.chat_id, text='Не умею делить на ноль.')
    else:
        data = data_from_user.split(operation_sign)
        result = operations_dict[operation_sign](int(data[0]), int(data[1]))
        bot.sendMessage(update.message.chat_id, text=result)


def main():
    updater = Updater(api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_counter))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
