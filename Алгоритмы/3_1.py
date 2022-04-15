# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

my_list = [2 * 0 for i in range (8)]
nat = [2 + i for i in range (99)]
def krat():
    for i in range(2,100):
        for j in range(2,10):
            if i % j == 0:
                my_list[j-2] += 1
    return my_list

print(krat())
