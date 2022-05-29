my_file = open('nginx_logs.txt', 'r', encoding= 'utf-8')
list_tup = []

for line in my_file:
    line = my_file.readline().split('-')
    tup_1 = str(line[0])[:-1]
    my_get = line[2].split('"')
    tup_2 = str(my_get[1][:3])
    my_get = my_get[1].replace('GET /', '')
    tup_3 = str(my_get.replace('HTTP/1.1', '')[:-1])
    my_tuple = (tup_1, tup_2, tup_3)
    list_tup.append(my_tuple)

my_file.close()

with open('find_spam.txt', 'w', encoding='utf-8') as f:
    for i in list_tup:
        f.write(str(i)+'\n')

my_gen = (i for i in list_tup)

for i in range(100):
    print(next(my_gen))

