from Node import Node

class DoublyLinkedList:
    def __init__(self, head = None, tail = None, count = 0):
        self.head = head
        self.tail = tail
        self.__count = count


    def Add(self, newdata):
        node = Node(newdata)
        self.__count += 1
        if self.head is None:
            self.head = node
            return
        self.tail = self.head
        node.previous = self.tail
        while(self.tail.next):
            self.tail = self.tail.next
        self.tail.next = node


    def DeleteFirst(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.previous = None
    

    
    def Print(self):
        printv = self.head
        while printv is not None:
            print(printv.data)
            printv = printv.next