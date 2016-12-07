people = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


def find_person(person_list, person_name):
    i=0
    while i<len(person_list):
        if person_list[i] == person_name:
            print("{} нашелся".format(person_name))
            break
        i+=1
        if i == len(person_list):
            print("{} не нашелся".format(person_name))
          

find_person(people, "Валера")
find_person(people, "Паша")


dialog = {"как дела?" : "Хорошо",
"как погода?" : "Обожаю метель",
"сколько время?" : "Не подскажу",
"как тебя зовут?" : "R2-D2",
"сколько тебе лет?" : "Я молод"}


def ask_user():
  while True:
    response = input("Напиши как твои дела? Или давай свой вопрос ").lower()
    if response == "хорошо":
      break
    else:
      print(get_answer(response))


def get_answer(response):
  return dialog.get(response)
  
ask_user()

