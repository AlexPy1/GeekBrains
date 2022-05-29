prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
new_list = []
rub = 0
cop = 0

#A
for i in range(len(prices)):
    prices[i] = float(prices[i])
for i in prices:
    if type(i) == float:
        ind = str(i).index(".")
        i = str(i)
        rub = i[0:ind]
        cop = i[ind+1:]
        new_list.append(rub)
        new_list.append('руб')
        if len(str(cop)) < 2:
            cop = str(cop) + '0'
            new_list.append(cop)
            new_list.append('коп,')
        else:
            new_list.append(cop)
            new_list.append('коп,')
print(' '.join(new_list))

#B

print(id(prices))
prices.sort()
print(prices)
print(id(prices))

#C
print(id(prices))
prices = sorted(prices, reverse= True)
print(prices)
print(id(prices))

#D
print(prices[0:5])