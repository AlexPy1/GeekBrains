my_dict = {}
count = 1
res = {}
with open('find_spam.txt', 'r', encoding='utf-8') as lines:
    for line in lines:
        line = line.split(',')
        line = line[0].replace('(','')
        if line in my_dict.keys():
            my_dict[line]+=1
        else:
            count=1
            my_dict[line] = count
for k,v in my_dict.items():
    if v > count:
        count = v
        res.clear()
        res[count] = k

print('Спамер:',res[count])