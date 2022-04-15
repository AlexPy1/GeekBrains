# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)
def num_rev(num:int) -> int:
    cnt = 0
    new_num = 0
    num1 = num
    while num > 0:
        num = num // 10
        cnt +=1

    while cnt >= 1:
        new_num += (num1 % 10) * 10**(cnt-1)
        cnt -= 1
        num1 = num1 // 10

    return new_num

print(num_rev(352))
print(num_rev(35278))
print(num_rev(35))

