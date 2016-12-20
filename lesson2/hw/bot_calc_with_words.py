import operator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(bot, update):
    bot.sendMessage(update.message.chat_id, text="write a math expression")


def calculator(bot, update):
    dict_words = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10',
    }

    dict_actions = {
        'addition': operator.add,
        'subtraction': operator.sub,
        'multiply': operator.mul,
        'divided': operator.truediv,
    }

    data_from_user = update.message.text
    ad1 = int(dict_words.get(data_from_user.split()[0]))
    ad2 = int(dict_words.get(data_from_user.split()[2]))
    result = dict_actions.get(data_from_user.split()[1])(ad1, ad2)
    bot.sendMessage(update.message.chat_id, text=result)


def main():
    updater = Updater("317888874:AAE8I5_laMUuF1SPN7wrk2TVZgLzDSuWVXg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], calculator))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
