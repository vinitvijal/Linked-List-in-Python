class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def InsertStart(self, newData):
        k = Node(newData)
        k.next = self.head
        self.head = k

    def InsertEnd(self, newData):
        k = Node(newData)

        if self.head.next == None:
            self.head.next = k
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = k

    def InsertAtPos(self, newData, pos):

        if pos == 0:
            self.InsertStart(newData)
            return 
        k = Node(newData)    
        curPos = 0
        current = self.head
        last = None
        while curPos != pos:
            last = current
            current = current.next
            curPos += 1
        last.next = k
        k.next = current





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
a.next = b 
b.next = c

LL = LinkedList()
LL.head = a


LL.InsertStart('1')
LL.InsertEnd("4")
LL.InsertStart("2")
LL.InsertEnd("5")
LL.InsertAtPos('COCO', 2)

LL.print_LL()