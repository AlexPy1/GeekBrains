import unittest

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь. 153
def sum_three(a: int) ->  int:
    sum = 0
    for i in range(3):
        sum += a % 10
        a = a // 10
    return sum


print(sum_three(250))
print(sum_three(780))
print(sum_three(711))
print(sum_three(732))

def mult_three(a: int) -> int:
    sum = 1
    for i in range(3):
        sum *= a % 10
        a = a // 10
    return sum

print(mult_three(250))
print(mult_three(780))
print(mult_three(711))
print(mult_three(732))


class MyTest(unittest.TestCase):  # почему то тесты не работают
    def sum_three_test(self):
        self.assertEqual(15, sum_three(780))
        self.assertEqual(9, sum_three(711))
        self.assertEqual(12, sum_three(732))





