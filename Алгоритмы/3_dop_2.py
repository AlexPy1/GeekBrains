# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self. size = 0
        self.head = ListNode(0)

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return

        curr = self.head
        for i in range (index +1):
            curr = curr.next

        return curr.val


    def AddAtIndex(self, index:int, val:int):
        if index < 0 or index > self.size:
            return
        self.size += 1
        prev = self.head
        for i in range (index):
            prev = prev.next

        to_add = ListNode(val)
        to_add.next = prev.next
        prev.next = to_add

    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return
        prev = self.head
        self.size -= 1
        for i in range(index):
            prev = prev.next

        prev.next = prev.next.next

    def AddAtHead(self, val:int):
        self.AddAtIndex(0, val)

    def AddAtTail(self, val:int):
        self.AddAtIndex(self.size, val)
    def print(self):
        curr = self.head.next
        while curr is not None:
            print(curr.val, end= ' ')
            curr = curr.next
        print()

    def MidleNode(self):
        cnt = 0
        curr = self.head.next
        while curr is not None:
            cnt += 1
            curr = curr.next
        if cnt % 2 == 0:
            cnt +=1
        stop = cnt // 2
        curr = self.head.next
        while stop > 0:
            stop -=1
            curr = curr.next
        return curr.val

myList = MyLinkedList()
myList.AddAtTail(5)
myList.AddAtTail(4)
myList.AddAtTail(3)
myList.AddAtTail(2)
myList.AddAtTail(1)
myList.AddAtTail(0)
myList.AddAtTail(-1)


myList.print()
print(myList.MidleNode())