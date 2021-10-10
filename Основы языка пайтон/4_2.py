from requests import get

def currency_rates(val):
    val = val.upper()
    new_list = []
    my_list = []
    my_dict = {}

    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    response = response.split('CharCode')
    for i in response:
        new_list += i.split('Name')

    for i in new_list:
        i = i.replace('><Value>', ' ')

        my_list += i.split('Value')


    i = 0
    while i + 5 < len(my_list):
        a = my_list[i + 1].replace('</', ' ')
        a = a[1:4]
        c = my_list[i + 4]
        c = c[:-2]
        c = c.split(',')
        c = float(c[0]) + (float(c[1])* 0.0001)

        my_dict.setdefault(a, c)
        i += 5
    print(type(my_dict.get(val)))
    return my_dict.get(val)


print(currency_rates("usd"))
print(currency_rates('EUR'))
print(currency_rates('dds'))

