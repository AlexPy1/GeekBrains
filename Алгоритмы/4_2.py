# Написать код для задачи: "Обработка сетевых пакетов", которую обсудили в конце семинара, условие здесь:


from collections import deque
queue = deque()
size, count = map(int, input().split())
for i in range(count):
    arrival, duration = map(int, input().split())
    if not queue:
        print(duration)
        queue.append(duration)
        continue
    if len(queue) < size:
        queue.append(duration)
    if queue[0] <= arrival:
        queue.popleft()



    if len(queue) < size:
        if queue:
            arrival = max(arrival,queue[-1])
        print(arrival)
        queue.append(arrival+duration)
    else:
        print(-1)

