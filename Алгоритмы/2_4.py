#  Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
#  равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
def check_nat(n:int) -> bool:
    sum = 0
    for i in range(1,n+1):
        sum += i
    j = n*(n+1)/2
    return sum == j

print(check_nat(5))
print(check_nat(555))
print(check_nat(378))
print(check_nat(216))
print(check_nat(23))

