my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']
new_list = [ ]

for i in my_list:
    if i.isdigit() == True:
        if int(i) < 10:
            i = "'" + '0' + str(i) + "'"
            new_list.append(i)

        else:
            i = "'" + i + "'"
            new_list.append(i)
    elif i[0] ==  '-' or i[0] == '+':
        if len(i) <= 2:
            i = "'" + i[0] + '0' + i[1] + "'"
            new_list.append(i)
        else:
            new_list.append(i)
    else:
        new_list.append(i)
print(" ".join(new_list))


