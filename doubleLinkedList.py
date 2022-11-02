class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertAtBeg(self,data):
        newnode = Node(data)
        
        if self.head == None:
            self.head = self.tail = newnode
           
        else:
            newnode.prev = None
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            
        self.length += 1
        
            
    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.head == None:
            self.insertAtBeg(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            newnode.prev = current
            current.next = newnode
            
            self.length += 1
            
           
    def insertAtMiddle(self, index, data):
        newnode = Node(data)
        if self.head == None or index == 0:
            self.insertAtBeg(data)
        ctr = 0
        current = self.head
        while current.next:
            if ctr == index - 1:
                newnode.next = current.next
                newnode.prev = current
                current.next = newnode
                current.next.prev = newnode
                self.length += 1
                
            current = current.next
            ctr += 1
        

    def deleteAtBeg(self):
        if self.head == None:
            print("It's empty")
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            
        
      #delete at middle and at end
        
    def delete(self, index):
        if index >= self.length or index < 0:
            print("It's empty")

        elif index == 0:
            self.deleteAtBeg()
        else:
            current = self.head
            previous = self.head
            ctr = 0
            while current.next!= None  or  ctr < index:
                if ctr == index:
                    
                    previous.next = current.next
                    current.next.prev = previous
                    
                    self.length -= 1
                    return
                    
                else:
                    previous = current
                    current = current.next
                    ctr += 1
    def print(self):
        if self.head == None:
            print("It's empty")
            return
        curr = self.head
        linked = " "
        while curr:
            linked += " <--[" + str(curr.data) + "]--> "
            curr = curr.next
        print(linked)
        print("length: ",self.length)
        
        



        
if __name__ == '__main__':

    l = DoubleLinkedList()
    l.insertAtBeg(3)
    l.insertAtBeg("section1")
    l.insertAtEnd("dsa")
    l.insertAtMiddle(1, "text editor")
    #l.deleteAtBeg()
    l.print()
    #l.deleteAtBeg()
    
    l.delete(2)
    l.print()
    

    
                
                
                
        
        
        
                
            






























    
        
        

        
        
