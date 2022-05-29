class MyErr(Exception):
    def __init__(self,text):
        self.text = text

my_list = []

def check_dig(x):
    try:
        if x.isdigit():
            my_list.append(x)
        else:
            raise MyErr('Вводить можно только числа!')
    except MyErr as err:
        print(err)

a = 0
while a != 'q':
    a = input('Введите число: ')
    check_dig(a)


print(my_list)