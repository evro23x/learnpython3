user_info = {"first_name": "engeny", "last_name": "gurov"}
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
user_info["first_name"] = first_name
user_info["last_name"] = last_name
print("Здравствуйте, " + user_info.get("first_name") + " " + user_info.get("last_name") + "!")
