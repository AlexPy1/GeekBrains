# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def check_num(num:int):
    chet = 0
    nechet = 0
    while num > 0:
        if (num % 10) % 2 == 0 or  num == 0:
            chet += 1
            num = num // 10
        else:
            nechet += 1
            num = num // 10
    return f'Четных {chet}, нечетных {nechet}'

print(check_num(34560))
print(check_num(2468264))
print(check_num(315420))