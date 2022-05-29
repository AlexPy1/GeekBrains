def my_func(count):
   my_gen = (i for i in range(1, count+1) if i % 2 != 0)
   return my_gen

for i in my_func(int(input())):
    print(i)

