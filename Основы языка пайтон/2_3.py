my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']
new_list = [ ]
print(id(my_list))
for i in range(len(my_list)):
    c = str(my_list[i])
    if my_list[i].isdigit() == True:
        if int(my_list[i]) < 10:
            b = 0
            b = "'" + '0' + str(my_list[i]) + "'"
            my_list[i] = b

        else:
            b = "'" + my_list[i] + "'"
            my_list[i] = b
    elif c[0] ==  '-' or c[0] == '+':
        if len(c) <= 2:
            b = "'" + c[0] + '0' + c[1] + "'"
            my_list[i] = b
        else:
            my_list[i] = c
    else:
        my_list[i] = c
print(" ".join(my_list))
print(id(my_list))