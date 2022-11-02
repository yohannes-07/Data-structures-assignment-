#we use linked list as its size isn't limited

from LinkedList import LinkedList

class Stack:

    def __init__(self):
        self.stack =  LinkedList()
        
     # WE PUSH ELEMENTS AT THE BEGININNING
     
    def push(self, data):
        self.stack.insertAtBeg(data)
        
    #WE POP ELEMETNS AT THE BEGININNING
        
    def pop(self):
        if self.stack.head.next:
            last_element = self.stack.head.data
            self.stack.deleteAtBeg()
            return last_element
    
    def isEmpty(self):
        return self.stack.head.next == None
    
    def peek(self):
        return self.stack.head.data
    
    
    def length(self):
        return self.stack.length



if __name__ == '__main__':
    s = Stack()

    s.push("section 1")
    s.push("text editor")
    s.push(789)
    s.push("&")
    
    print(s.pop())
    print(s.isEmpty())
    print(s.peek())
    print(s.length())
