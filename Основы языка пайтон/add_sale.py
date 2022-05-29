from sys import argv
count =argv[1]

my_file = open('bakery.csv','a', encoding='utf-8')
my_file.write(f'{count}\n')
