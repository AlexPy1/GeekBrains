import os
main = 'my_project'
sub = ['settings', 'mainapp', 'adminapp','authapp']

my_dict = {main:sub}


def create_folder(main, sub):
    dir_path = os.path.join(main, sub[0])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        for i in sub:
            if i == sub[0]:
                continue
            else:
                dir_path = os.path.join(main, i)
                os.mkdir(dir_path)
    else:
        exit('Стартер уже создан')


create_folder(main, sub)



