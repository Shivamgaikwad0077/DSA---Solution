class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtFront(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def printLL(self):
        t = self.head
        while(t.next != None):
            print(t.data , end="<--->")
            t = t.next
        print(t.data)

obj = doublyLinkedList()
obj.insertAtEnd(15)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtFront(10)
obj.insertAtFront(5)
obj.printLL()