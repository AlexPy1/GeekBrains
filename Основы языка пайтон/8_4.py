from functools import wraps
def val_checker(ch=0):
    def _cheker(calc_cube):

        @wraps(calc_cube)
        def chek(x):
            if ch(x) == 1:
                msg = 'Меньше нуля'
                raise ValueError(msg)
            else:
                return calc_cube(x)
        return chek
    return _cheker



@val_checker(lambda x: x<0)
def calc_cube(x):
   return x ** 3

try:
    a = calc_cube(3)
    print(a)
    a = calc_cube(2)
    print(a)
    a = calc_cube(-6)
    print(a)
except ValueError:
    print('Ошибка. Меньше нуля.')