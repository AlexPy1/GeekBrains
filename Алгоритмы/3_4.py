# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def two_min(arr:list):
    min_1 = arr[0]
    pl_mn_1 = 0
    min_2 = arr[1]
    pl_mn_2 = 0
    for i in range(len(arr)):
        if arr[i] < min_1:
            min_1 = arr[i]
            pl_mn_1 = i

    for i in range(len(arr)):
        if arr[i] < min_2 and i != pl_mn_1:
            min_2 = arr[i]
            pl_mn_2 = i
    return (min_1, pl_mn_1),(min_2, pl_mn_2)

print(two_min([1,2,3,4,5,6,0,4,3,2,4,5,6,7,3]))