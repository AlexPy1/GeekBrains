def num_translate_adv(number):
    if number[0] == 'O' or number[0] == 'T' or number[0] == 'F' or number[0] == 'S' or number[0] == 'E' or number[0] == 'N':

        numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                   'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight':
                       'восемь', 'nine': 'девять', 'ten': 'десять'}

        res = numbers.get(str(number).lower())
        print(res.title())
    else:
        numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                   'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight':
                       'восемь', 'nine': 'девять', 'ten': 'десять'}
        print(numbers.get(number))

a = input('Введите число: ')

num_translate_adv(a)

