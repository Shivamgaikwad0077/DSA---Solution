class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

 #making class of singlyLinkedlist   
class singlyLinkedList:
    def __init__(self,head=None):
        self.head = head
    
    #inserting element at the end
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp


    #inserting element at front
    def inseratFront(self,value):
        temp = Node(value)
        if(self.head != None):
            temp.next = self.head
            self.head = temp

    #inserting element at middle
    def insertAtMiddle(self,value,element):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == element):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

        
    """deleting element functions
    for deleting any element from linked list we have to se the two pointer that is 
    "prev" and "t1" 
    if t1 = self.head means  ([1]-[2]-[3]) t1 points  first elemenet and prev elements also point t1 i.e """
    def delelement(self,value):
        t1 = self.head
        prev = t1
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next

   #printing functions 
    def printLn(self):
     t1 = self.head
     while(t1 != None):
        print(f"[{t1.data} | • ]", end=" → ")
        t1 = t1.next

    

#calling objects through classes
obj = singlyLinkedList()
obj.insertAtEnd(20)
obj.insertAtEnd(40)
obj.insertAtEnd(60)
obj.inseratFront(15)
obj.inseratFront(10)
obj.insertAtMiddle(30,20)
obj.insertAtMiddle(35,30)
obj.delelement(15)
obj.printLn()