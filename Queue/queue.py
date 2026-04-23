class Queue:
    def __init__(self):
        self.queue = []

    #checking if Queue is empty
    def isempty(self):
        return len(self.queue) == 0
    
    # Inserting element at rare(last) Enque
    def Enque(self,value):
        self.queue.append(value)
        print(value , "Inserted into the queue")
    
    # Delete element at front Deque
    def Deque(self):
        if self.isempty():
            print("Queue is empty ")
        else:
            print(self.queue.pop(0) , " :  is front element removed from queue")
    
    #display anything 
    def display(self):
        print("Front →", " → ".join(map(str, self.queue)), "→ Rear")

Q = Queue()
Q.Enque(5)
Q.Enque(10)
Q.Enque(15)
Q.Enque(20)
Q.Enque(25)
Q.Enque(30)
Q.display()
Q.Deque()
Q.display()
Q.Deque()
Q.display()    
             

