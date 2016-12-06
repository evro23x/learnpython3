string = input("insert data: ")
for i in string:
    print(i)


def avg(scores):
    return sum(scores) / len(scores)*1.0


rating = [{'school_class': '4a', 'scores': [5, 5, 5, 5, 5]},
          {'school_class': '4b', 'scores': [5, 5, 5, 5, 5]},
          {'school_class': '5a', 'scores': [5, 5, 3, 4, 5]},
          {'school_class': '5b', 'scores': [4, 5, 4, 5, 3]},
          {'school_class': '6a', 'scores': [3, 5, 3, 5, 3]},
          {'school_class': '6b', 'scores': [5, 4, 3, 5, 5]},
          {'school_class': '7a', 'scores': [5, 3, 3, 4, 5]},
          {'school_class': '7b', 'scores': [5, 5, 5, 5, 5]}]
school_avg = []
for current_class in rating:
    class_avg = int(avg(current_class.get('scores')))
    print('avg for class {} = {}'.format(current_class.get('school_class'), class_avg))
    school_avg.append(class_avg)
print('avg for school = {}'.format(int(avg(school_avg))))

