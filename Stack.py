class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size
    
    #pushing element function
    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack is overflow")
        else:
            self.stack.append(value)
            print(value, "Inserted into stack")
    
    #poping elemenet function
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            removed = self.stack.pop()
            print(removed,"popped from stack")
    
    #to see top element in stack
    def peek(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            print("Top element is : ", self.stack[-1])
    
    #display the overall stack element 
    def display(self):
        print("Stack (top → bottom):")
        for item in reversed(self.stack):
            print(item)
    

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.display()
s.peek()
s.pop()
s.display()