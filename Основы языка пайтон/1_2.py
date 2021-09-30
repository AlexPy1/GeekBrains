# 17485588610
# 15392909930

coubs = []
sum_a = 0
sum_b = 0
sum = 0
b = 0

for i in range(1001):
    if i % 2 != 0:
         coub = i ** 3
         coubs.append(coub)
for i in coubs:
    b = i
    sum = 0
    while i != 0:
        num_1 = i % 10
        i = i // 10
        sum += num_1
    if sum % 7 == 0:
        sum_a += b
print(sum_a)

for i in range(len(coubs)):
    coubs[i] = coubs[i] + 17

for i in coubs:
    b = i
    sum = 0
    while i != 0:
        num_1 = i % 10
        i = i // 10
        sum += num_1
    if sum % 7 == 0:
        sum_b += b

print(sum_b)
