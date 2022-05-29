src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
my_list =[]

my_list =[src[i+1] for i in range(0,len(src)-1) if src[i+1] > src[i]]
print(my_list)
