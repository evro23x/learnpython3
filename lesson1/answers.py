dialog = {"привет": "И тебе привет!", "как дела": "Лучше всех", "котики": "котики, котики, все любят котиков", "пока": "Увидимся"}


def get_answer(key):
    return dialog.get(key)

while True:
    user_answer = (input("say anything: ").lower())
    print(get_answer(user_answer))
    if user_answer == "пока":
        break
