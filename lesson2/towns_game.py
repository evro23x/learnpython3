import random
import towns_db

# загружаем список городов в переменную
# производим поиск рандомного города и отдаем пользователю
# удаляем найденный город из списка городов
# получаем даные от пользователя
# валидируем полученные данные
# производим поиск города от пользователя в базе
# удаляем найденный город из списка городов
# производим поиск города в базе по последней букве города от пользовательского
# удаляем найденный город из списка городов
# отправляем найденный город в чат/консоль


def load_towns_list():
    return towns_db.towns_dict


def search_town(towns, previous_town=None, town_from_user=None, from_user=False, rand=False):
    if rand:
        town = towns_db.towns_dict[random.randint(0, len(towns_db.towns_dict))]
        remove_data_from_dict(towns, town)
        return town

    if from_user:
        if validate_town_name(town_from_user):
            if previous_town[-1] == town_from_user[0:1]:
                for town in towns:
                    if town.lower() == town_from_user:
                        remove_data_from_dict(towns, town)
                        return town
                return False
    else:
        for town in towns:
            if town[0:1].lower() == prepare_word(previous_town)[-1]:
                remove_data_from_dict(towns, town)
                return town


def validate_town_name(data):
    first_latter_data = data[0:1]

    if first_latter_data in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        return True
        # return "Нет такого города"

    elif first_latter_data in "abcdefghijklmnopqrstuvwxyz":
        return False
        # return "Используй русские символы"

    elif first_latter_data in "1234567890":
        return False
        # return "Цифры? Ты серьезно?"

    elif len(first_latter_data) < 1 or first_latter_data == ' ':
        return False
        # return "Лишние пробелы убери"

    else:
        return False
        # return "Предлагаю играть используя русский язык!"


def remove_data_from_dict(towns, data):
    towns.remove(data)


def prepare_word(word):
    ban_symbol = 'ьъйы'
    if word[-1] in ban_symbol:
        return word[0:-1]
    else:
        return word

towns_list = load_towns_list()
previous_town = prepare_word(search_town(towns_list, rand=True))
print("Поиграем в города(договоримся играть без городов на буквы 'Ь', 'Ъ', 'Й', 'Ы')\n"
      "Я начинаю, город - {}, тебе на {}".format(previous_town, previous_town[-1].upper()))
while True:

    user_answer = (input("Твой ход : ")).lower()
    search_result = search_town(towns_list, previous_town, user_answer, from_user=True)

    if not search_result:
        print("Либо город уже использовался в игре, либо такого города не существует")
    else:
        response = search_town(towns_list, search_result)
        print("Мне на {} - {}, тебе на {}"
              .format(prepare_word(user_answer)[-1].upper(), response, prepare_word(response)[-1].upper()))
        previous_town = prepare_word(response)

    if user_answer == "exit":
        break
