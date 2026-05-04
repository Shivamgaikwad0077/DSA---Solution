class Dequeue:
    def __init__(self):
        self.q = []
    
    def isempty(self):
        return len(self.q) == 0
    
    def insertAtfront(self,value):
        self.q.insert(0,value)
        print("Inserted value is : ", value)
    
    def deleteAtfront(self):
        if self.isempty():
            print("Dequeue is empty")
        else:
            print(self.q.pop(0), " : delete from front ")
    
    def insertAtEnd(self,value):
        self.q.append(value)
        print("Inserted value is :" , value)
    
    def deleteAtend(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.q.pop, "deleted from end ")
    
    def display(self):
        print("Deque items ", self.q)
    
s = Dequeue()
s.insertAtfront(10)
s.insertAtfront(20)
s.insertAtfront(30)
s.insertAtEnd(40)
s.insertAtEnd(50)
s.insertAtEnd(5)
s.display()
s.deleteAtfront()
s.deleteAtend()
s.display()