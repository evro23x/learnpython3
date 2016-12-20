import operator

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

while True:
    user_answer = (input("write a math expression: ").lower())
    ad1 = int(dict_words.get(user_answer.split()[0]))
    ad2 = int(dict_words.get(user_answer.split()[2]))
    print(dict_actions.get(user_answer.split()[1])(ad1, ad2))
    if user_answer == "exit":
        break
