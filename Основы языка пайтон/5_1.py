def my_func(count):
    for i in range(1, count+1):
        if i % 2 != 0:
            yield i

name = my_func(int(input()))


for i in name:
    print(i)

print(next(name))