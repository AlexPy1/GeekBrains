# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def sum_check(list_num:list):
    i1 = 0
    sum1 = 0
    for i in list_num:
        num1 = i
        sum = 0
        while num1 > 0:
            sum += num1 % 10
            num1 = num1 // 10

        if sum > sum1:
            sum1 = sum
            i1 = i
    return sum1, i1

list_num = [10, 155, 99, 678]

print(sum_check(list_num))