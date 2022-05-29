from functools import wraps

def type_logger(calc_cube):

    @wraps(calc_cube)

    def tag_logger(*args,**kwargs):


        res =''
        if kwargs:
            for x,i in kwargs.items():
                my_t = type(i)
                res += f'{calc_cube.__name__}({i}: {my_t}), '
            return res
        else:

            for i in args:
                my_t = type(i)
                res += f'{calc_cube.__name__}({i}: {my_t}), '
            return res

    return tag_logger


@type_logger
def calc_cube(x):
    return x ** 3



print(calc_cube(x=1, y= 4))



