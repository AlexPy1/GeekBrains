def get_parent(index: int):
    return (index - 1) // 2


def get_left(index: int):
    return index * 2 + 1

def get_right(index:int):
    return index * 2 + 2

class Heap:
    def __init__(self):
        self.array = []

    def sift_down(self,index:int):
        min_index = index
        left = get_left(index)
        right = get_right(index)
        if left < len(self.array) and self.array[left] < self.array[min_index]:
            min_index = left
        if right < len(self.array) and self.array[right] < self.array[min_index]:
            min_index = right
        if index != min_index:
            self.array[index], self.array[min_index] = self.array[min_index], self.array[index]
            self.sift_down(min_index)


    def sift_up(self,index:int):
        while index > 0 and self.array[get_parent(index)] > self.array[index]:
            self.array[index], self.array[get_parent(index)] = self.array[get_parent(index)], self.array[index]
            index = get_parent(index)

    def add(self, val:int):
        self.array.append(val)
        self.sift_up(len(self.array) -1)

    def extract_min(self):
        min = self.array[0]
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.array.pop()
        self.sift_down(0)
        return min


    def get_size(self):
        return len(self.array)


# arr = input().split()
# for i in range(len(arr)):
#     arr[i] = int(arr[i])

# heap = Heap()
# for num in arr:
#     heap.add(num)
#
# for i in range(heap.get_size()):
#     print(heap.extract_min(), end=' ')

#  Реализовать параллельную обработку пакетов


queue = Heap()
n, m = map(int, input().split())
time = input().split()

for i in range(n):
    queue.add([0, i])

for task in range(m):
    curr = queue.extract_min()
    print(*reversed(curr))
    curr[0] += int(time[task])
    queue.add(curr)


