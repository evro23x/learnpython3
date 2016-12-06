def str_check(str1, str2):
    if str1 == str2:
        return 1
    elif not str1 == str2 and str2 == 'learn':
        return 3
    elif not str1 == str2 and len(str1) > len(str2):
        return 2


while True:
    string1 = (input("write first string: ").lower())
    string2 = (input("write second string: ").lower())
    print('Return value is: {}'.format(str_check(string1, string2)))
    if string2 == "exit":
        break

