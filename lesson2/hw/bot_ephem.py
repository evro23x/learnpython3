import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def new_moon(bot, update):

    dfu = update.message.text

    moon = {
        "Предыдущий цикл": {
            "Последняя четверть луны": ephem.previous_last_quarter_moon(dfu),
            "Новолуние": ephem.previous_new_moon(dfu),
            "Первая четверть луны": ephem.previous_first_quarter_moon(dfu),
            "Полнолуние": ephem.previous_full_moon(dfu),
        },
        "Следующий цикл": {
            "Последняя четверть луны": ephem.next_last_quarter_moon(dfu),
            "Новолуние": ephem.next_new_moon(dfu),
            "Первая четверть луны": ephem.next_first_quarter_moon(dfu),
            "Полнолуние": ephem.next_full_moon(dfu),
        }

    }

    for key in moon:
        bot.sendMessage(update.message.chat_id, text=key)
        for row_key in moon[key]:
            bot.sendMessage(update.message.chat_id, text=(row_key, ":", moon[key][row_key]))


def main():
    updater = Updater("317888874:AAE8I5_laMUuF1SPN7wrk2TVZgLzDSuWVXg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", new_moon))
    dp.add_handler(MessageHandler([Filters.text], new_moon))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
