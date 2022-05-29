from itertools import zip_longest
from sys import argv
file_1 = argv[1]
file_2 = argv[2]
file_res = argv[3]

name = open(file_1, 'r', encoding='utf - 8')
hob = open(file_2, 'r', encoding='utf - 8')

name_list = (line.replace('\n', '') for line in name)

hob_list = (line_2.replace('\n', '') for line_2 in hob)

my_dict = {i:n if i != None else exit(1) for i,n in zip_longest(name_list, hob_list)}

name.close()
hob.close()

with open(file_res, 'w', encoding='utf-8') as r:
    for k,v in my_dict.items():
        r.write(f'{k}: {v}\n')
