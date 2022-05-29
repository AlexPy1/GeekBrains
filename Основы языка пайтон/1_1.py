durarion = int(input())

min = durarion // 60
hours = durarion // 3600
days = hours // 24
sec = durarion - min * 60

while sec > 60:
    sec -= 60

while min > 60:
    min -= 60

while hours > 24:
    hours -= 24


print(days, 'дн', hours, "час", min, "мин", sec, "сек")
