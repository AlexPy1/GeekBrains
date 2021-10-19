from sys import argv
if len(argv)>1:
    count = argv[1]
else:
    count = 0

if len(argv)>2:
    count_2 = int(argv[2])
else:
    count_2=999
a = 1
with open('bakery.csv', 'r', encoding='utf-8') as line:
    for lines in line:
        if a < int(count):
            a+=1
            continue
        else:
            print(lines, end='')
            a+=1
            if a > int(count_2):
                break

    else:
        for lines in line:
            print(lines, end='')