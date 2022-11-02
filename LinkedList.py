class node():
    def __init__ (self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def insertAtBeg(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.length += 1
        else:
            newnode.next = self.head
            self.head = newnode
            self.length += 1
    
    def deleteAtBeg(self):
        if self.head == None:
            return "It's empty"
        else:
            Temp = self.head.data
            self.head = self.head.next
            self.length-=1
            return Temp
    
    def insertAtEnd(self, data):
        newnode = node(data)
        if self.head == None:
            self.insertAtBeg(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode
            newnode.next = None
            self.length += 1
            
    
    def deleteAtEnd(self):
        if self.head == None:
            return "The list is empty"
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
        self.length-=1

    def peekLastElem(self):
        current = self.head
        for i in range(self.length):
            current = current.next
        return current.data
   

    def Empty(self):
        return self.head == None

    
