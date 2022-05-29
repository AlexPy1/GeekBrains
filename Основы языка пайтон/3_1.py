def num_translate(number):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three':'три', 'four':'четыре',
               'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight':
                   'восемь', 'nine': 'девять', 'ten': 'десять'}
    return numbers.get(number)

print(num_translate(input('Введите число: ')))


