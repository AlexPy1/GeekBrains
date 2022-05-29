class MyErr(Exception):
    def __init__(self, text):
        self.text = text

a = input('Введите первое значение: ')
b = input('Введите второе значение: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyErr('На ноль делить нельзя!')
except (ValueError, MyErr) as err:
    print(err)

else:
    print(a/b)