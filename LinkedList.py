from Node import Node

class LinkedList:
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
        while(self.tail.next):
            self.tail = self.tail.next
        self.tail.next = node
        


    def Remove(self, data):
        current = self.head
        
        if (current is not None):
            if (current.data == data):
                self.head = current.next
                current = None
                return
        while(current is not None):
            if (current.data == data):
                break
            previous = current
            current = current.next

        if (current == None):
            return

        previous.next = current.next
        current = None
        self.__count -= 1
    

    def Count(self): 
        print(self.__count)


    def IsEmpty(self):
        print(self.__count == 0)


    def Print(self):
        printv = self.head
        while printv is not None:
            print(printv.data)
            printv = printv.next


    def Clear(self):
        self.head = None
        self.tail = None
        self.__count = 0

    
    def Constains(self, data):
        current = self.head
        while (current is not None):
            if (current.data == data):
                print(True)
            current = current.next
        print(False)


    def AppendFirst(self, newdata):
        node = Node(newdata)
        node.next = self.head
        self.head = node
        if (self.__count == 0):
            self.tail = self.head
        self.__count += 1

    