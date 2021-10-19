from itertools import zip_longest

name = open('users.csv', 'r', encoding='utf - 8')
hob = open('hobby.csv', 'r', encoding='utf - 8')

name_list = (line.replace('\n', '') for line in name )

hob_list = (line_2.replace('\n', '') for line_2 in hob)

my_dict = {i:n if i != None else exit(1) for i,n in zip_longest(name_list, hob_list)}

name.close()
hob.close()
with open('6_3_res.txt', 'w', encoding='utf-8') as r:
    for k,v in my_dict.items():
        r.write(f'{k}: {v}\n')

