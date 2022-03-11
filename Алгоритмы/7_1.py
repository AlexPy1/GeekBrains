# 1. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках
def mid_check(array):
    def quick_sort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i < pivot]
            greater = [i for i in array[1:] if i > pivot]
            return quick_sort(less) + [pivot] + quick_sort(greater)
    return quick_sort(array)
    # return array[len(array) // 2]

print(mid_check([3,4,1,2,3,4,5,1,6,7])) # 1 1 2  3 3 4 4 5