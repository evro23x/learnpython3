from datetime import datetime
time = str(datetime.today())
text = input("Введите запись: ")
f = open("parsed_page", "w")
f.write(time + "\n")
f.write(text + "\n")
f.write("\n")
f.close()
