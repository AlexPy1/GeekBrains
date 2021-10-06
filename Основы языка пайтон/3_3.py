def thesaurus(*args):
    my_dict ={}
    sorted(args)
    for i in args:
        if i[0] in my_dict.keys():
            a = my_dict.get(i[0])
            b = [a, i]
            my_dict[i[0]] = b
        else:
            my_dict.setdefault(i[0], i)
    print(my_dict)
thesaurus("Иван", "Мария", "Петр", "Илья", 'Петя')