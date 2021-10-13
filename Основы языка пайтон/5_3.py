from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена']
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

while len(tutors) < len(klasses):
    klasses.pop()
my_gen = (i for i in zip_longest(tutors,klasses))

for i in my_gen:
    print(i)

print(next(my_gen))