# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
def cnt_n(ch1:str, n:int) -> int:
    cnt = 0
    for i in ch1:
        if i == n:
            cnt +=1
    return f'Цифра {n} встречается {cnt} раз'
ch1 = input('Введите число')
n = input('Введите цифру для проверки вхождений')

print(cnt_n(ch1, n))