#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def swap_min_max(a:list):
    min = a[0]
    mn_pl = 0
    max = a[0]
    mx_pl = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            mx_pl = i
        if a[i] < min:
            min = a[i]
            mn_pl = i
    a[mn_pl], a[mx_pl] = a[mx_pl], a[mn_pl]
    return a

print(swap_min_max([2,5,9,2,4,3,1,2,3]))
