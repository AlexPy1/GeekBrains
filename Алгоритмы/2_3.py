# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
def sum_n(n:int):
    sum = 0
    next_d = 1
    while n > 0:
        sum += next_d
        next_d *= -0.5
        n -= 1
    return sum

n = int(input('Введите число'))
print(sum_n(n))

