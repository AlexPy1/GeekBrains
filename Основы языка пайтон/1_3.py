proc = 'процент'
num = int(input())


if num % 10 == 1 and num != 11:
    print(num, proc)
elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
    if num != 12 and num != 13 and num != 14:
        print(num, proc + 'а')
    else: print(num, proc + 'ов')

else:
    print(num, proc + 'ов')

