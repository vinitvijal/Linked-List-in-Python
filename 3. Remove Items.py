class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def removePos(self, pos):
        if pos == 0:
            self.head = self.head.next
            return
        curPos = 0
        prev = None
        current = self.head
        while curPos != pos:
            prev = current
            current = current.next
            curPos += 1
        current = current.next
        prev.next = current
        
        
    def removeItem(self, data):
        current = self.head
        prev = None
        if current.val == data:
            self.head = current.next
            return
        else:
            while current != None:
                if current.val == data:
                    current = current.next
                    prev.next = current
                    return
                prev = current
                current = current.next
            else:
                print('Item Not Found!!!')
        
    def print_LL(self):
        if self.head == None:
            print("Linked List is Empty")
        else:
            current = self.head
            while current != None:
                print(current.val)
                current = current.next


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

LL = LinkedList()
LL.head = a

LL.removePos(0)

LL.removeItem('Dj')

LL.print_LL()
        