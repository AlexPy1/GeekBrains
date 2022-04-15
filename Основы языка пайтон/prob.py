coubs = []
for i in range(1001):
    if i % 2 != 0:
         coub = i ** 3
         coubs.append(coub)
print(coubs[0:10])

for i in range(len(coubs)):
    coubs[i] = coubs[i] + 17
print(coubs[0:10])