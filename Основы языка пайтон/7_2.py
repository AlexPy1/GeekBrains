import os


with open('config.yaml', 'r', encoding='utf-8') as con:
    for i in con:
        if i[0].isalpha():
            i = i.strip()
            dir_path_one = os.path.join(i[:-1])
            os.mkdir(dir_path_one)
        elif i[2].isalpha():
            i = i.strip()
            dir_path_two = os.path.join(dir_path_one,i[:-1])
            os.mkdir(dir_path_two)
        elif i[-4].isalpha() and not i.strip().endswith('.html'):
            i = i.strip()
            dir_path_two = os.path.join(dir_path_two, i[2:-1])
            os.mkdir(dir_path_two)
        else:
            i = i.strip()
            i=str(i[1:])
            dir_path_three = os.path.join(dir_path_two,i)
            with open(dir_path_three,'w', encoding='utf-8') as n:
                n.write('')



