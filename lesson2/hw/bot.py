import operator

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(bot, update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')


def word_counter(bot, update):
    print("Вызван /wordcount")
    amount_of_words = len(update.message.text.split())-1
    if amount_of_words > 0:
        bot.sendMessage(update.message.chat_id, text=amount_of_words)


def calculate(bot, update):
    print("Вызван /calculate")

    available_signs = '+-:/*'
    operations_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        ':': operator.truediv,
        '/': operator.truediv,
    }

    if update.message.text[-1] == '=':
        data_from_user = update.message.text[6:-1]
        operation_sign = None

        for sing in available_signs:
            if sing in data_from_user:
                operation_sign = sing
                break

        if operation_sign is None:
            bot.sendMessage(update.message.chat_id, text='Непонятное действие, я умею только такие: +-:*')
        elif operation_sign == ':' and data_from_user[-1] == '0':
            bot.sendMessage(update.message.chat_id, text='Не умею делить на ноль.')
        else:
            data = data_from_user.split(operation_sign)
            result = operations_dict[operation_sign](int(data[0]), int(data[1]))
            bot.sendMessage(update.message.chat_id, text=result)

        # operation_sign = get_operation_sign(data_from_user)
        # operands = get_operands(data_from_user, operation_sign)
        # operation_result = apply_operation(operation_sign, operands)
        # send_reply(operation_result)

            # print(update.message.text[6:])
            # bot.sendMessage(update.message.chat_id, text=update.message.text[6:])

            # amount_of_words = len(update.message.text.split())-1
            # if amount_of_words > 0:
            #     bot.sendMessage(update.message.chat_id, text=amount_of_words)


def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))


def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)


def main():
    updater = Updater("317888874:AAE8I5_laMUuF1SPN7wrk2TVZgLzDSuWVXg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_counter))
    dp.add_handler(CommandHandler("calc", calculate))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
