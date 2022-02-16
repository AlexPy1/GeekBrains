import unittest
# Определить, является ли год, который ввел пользователем, високосным или не високосным.
def year_check(a:int) -> bool:
    return a % 400 == 0 or a % 4 == 0 and a % 100 != 0

print(year_check(2020))
print(year_check(2022))
print(year_check(2021))

class MyTest1(unittest.TestCase): # Здесь тоже тесты не отрабатывают корректно.
    def year_check_test(self):
        self.assertEqual(True, year_check(2020))
        self.assertEqual(False, year_check(2021))
