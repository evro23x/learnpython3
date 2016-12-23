import towns_game_function as func

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    func.towns_list = func.load_towns_list()
    func.previous_town = func.prepare_word(func.search_town(func.towns_list, rand=True))
    hello = "Поиграем в города(договоримся играть без городов на буквы 'Ь', 'Ъ', 'Й', 'Ы')\n" \
            "Я начинаю, город - "+func.previous_town+", тебе на "+func.previous_town[-1].upper()+" "
    bot.sendMessage(update.message.chat_id, text=hello)


def new_game(bot, update):
    user_answer = update.message.text.lower()
    search_result = func.search_town(func.towns_list, func.previous_town, user_answer, from_user=True)
    if not search_result:
        bad_response = "Либо город уже использовался в игре, либо такого города не существует"
        bot.sendMessage(update.message.chat_id, text=bad_response)
    else:
        response = func.search_town(func.towns_list, search_result)
        good_response = "Мне на "+func.prepare_word(user_answer)[-1].upper()+" - "+response+", тебе на "+func.prepare_word(response)[-1].upper()+" "
        bot.sendMessage(update.message.chat_id, text=good_response)
        func.previous_town = func.prepare_word(response)


def main():
    updater = Updater("317888874:AAE8I5_laMUuF1SPN7wrk2TVZgLzDSuWVXg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], new_game))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
