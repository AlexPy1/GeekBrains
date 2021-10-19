from itertools import zip_longest

name = open('users.csv', 'r', encoding='utf - 8')
hob = open('hobby.csv', 'r', encoding='utf - 8')

name_list = (line.replace('\n', '') for line in name)

hob_list = (line_2.replace('\n', '') for line_2 in hob)


with open('6_4_res.txt', 'w', encoding='utf-8') as r:
    my_list=[i if i != None else exit(1) for i in zip_longest(name_list, hob_list)]
    for i in my_list:
        r.write(str(i[0])+': '+str(i[1])+'\n')


name.close()
hob.close()