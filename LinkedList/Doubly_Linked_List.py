class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None

    # insert at end
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t.next:
            t = t.next
        t.next = temp
        temp.prev = t

    # insert at front
    def insertAtFront(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    # insert after a given value
    def insertAfterValue(self, value, position):
        t = self.head

        while t:
            if t.data == position:
                temp = Node(value)

                temp.next = t.next
                if t.next:  # important check
                    t.next.prev = temp

                t.next = temp
                temp.prev = t
                return
            t = t.next

        print("Position value not found")

    # deletion
    def deletion(self, value):
        if self.head is None:
            print("Linked list is empty")
            return

        t = self.head

        # deleting head
        if t.data == value:
            self.head = t.next
            if self.head:
                self.head.prev = None
            return

        while t:
            if t.data == value:
                if t.next:
                    t.prev.next = t.next
                    t.next.prev = t.prev
                else:  # last node
                    t.prev.next = None
                return
            t = t.next

        print("Value not found")

    # print list
    def printLL(self):
        if self.head is None:
            print("List is empty")
            return

        t = self.head
        while t:
            print(t.data, end="<--->" if t.next else "")
            t = t.next
        print()

obj = doublyLinkedList()
obj.insertAtEnd(15)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtFront(10)
obj.insertAtFront(5)
obj.insertAtFront(1)
obj.insertAfterValue(50, 20)
obj.deletion(5)
obj.deletion(20)

obj.printLL()