import ephem

while True:
    user_answer = (input("date: ").lower())

    moon = {
        "Предыдущий цикл": {
            "Последняя четверть луны": ephem.previous_last_quarter_moon(user_answer),
            "Новолуние": ephem.previous_new_moon(user_answer),
            "Первая четверть луны": ephem.previous_first_quarter_moon(user_answer),
            "Полнолуние": ephem.previous_full_moon(user_answer),
        },
        "Следующий цикл": {
            "Последняя четверть луны": ephem.next_last_quarter_moon(user_answer),
            "Новолуние": ephem.next_new_moon(user_answer),
            "Первая четверть луны": ephem.next_first_quarter_moon(user_answer),
            "Полнолуние": ephem.next_full_moon(user_answer),
        }

    }

    for key in moon:
        print(key)
        for row_key in moon[key]:
            print(row_key, ":", moon[key][row_key])

    if user_answer == "exit":
        break
