'''
section 1
GROUP MEMBERS. ID
Yohannes Ahunm. UGR/4045/13
Semir Hamid UGR/9690/13
Natinael Abebaw UGR/7747/13
Zelalem Habtamu UGR/7301/13
Bilen Mehalek UGR/0252/13
Deribew Shimelis UGR/5307/13
Hayat shifa UGR/9771/13

'''

#We used double linked list to build some operations like write, delete(backspace)
#move the cursor forwar and backward as any text editor works

from doubleLinkedList import *
class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class TextEditor:
    def __init__(self, data):
        self.data = data
        self.leftLength = 0 # is is used to check how many characters are available to be delted or to move the cursor to the left
        self.head = Node(data = "|") #we symbolized the cursor by "|"

    def write(self, data): #writes one character each time this function is called
        
        newnode = Node(data)
        curr = self.head
          
        if curr.data == "|":
            newnode.prev = None
            
            newnode.next = self.head
            self.head.prev = newnode
            
            self.head = newnode
            self.leftLength += 1
            
        else:
            while curr:
                if curr.data == "|":
                    newnode.next = curr
                    newnode.prev = curr.prev
                    
                    curr.prev.next = newnode
                    curr.prev = newnode
                    self.leftLength += 1
                     
                curr = curr.next
        
                   
    def backspace(self): # deletes one character each time this function is called
        if self.leftLength == 0:
            self.printf()
        else:
            curr = self.head
            previous = self.head
            if curr.next.data == "|":
                self.head = self.head.next
                
            else:
        
                while curr:
                    if curr.next.data == "|":
                        previous.next = curr.next
                        curr.next.prev = previous
                        self.leftLength -= 1
                        break
                            
                    else:
                        previous = curr
                        curr = curr.next
                    
             
    def moveCursorLeft(self): # moves the cursor to the left every time this function is called
        if self.leftLength == 0:
            self.printf() # returns as it is if the cursor is at the leftmost postion
        else:  
            self.cursor = self.head
            previous = self.head
            while self.cursor:
                if self.cursor.data == "|":
                    self.cursor.data, previous.data = previous.data, self.cursor.data
                    self.leftLength -= 1
                else:
                    previous = self.cursor
                    self.cursor = self.cursor.next
                    

        
    def moveCursorRight(self): # moves the cursor to the right every time this function is called
        self.cursor = self.head
        
        while self.cursor:
            if self.cursor.data == "|" and self.cursor.next != None:
                self.cursor.data, self.cursor.next.data = self.cursor.next.data, self.cursor.data
                self.leftLength += 1
                break
            
            elif self.cursor.next == None: # returns if the cursor is the last element of the list
                self.printf()
                break
            else:
                self.cursor = self.cursor.next

                
    def printf(self): #converts the linked list to string to show how it works
        
        curr = self.head
        linked = ""
        while curr != None:
            linked +=  str(curr.data)
            curr = curr.next
        print(linked)
        #print("\nNo of left Characters: ",self.leftLength)


  
             
if __name__ == '__main__':

    txt = TextEditor(str)
    txt.printf()
    txt.write("A")
    txt.printf()
    txt.write("B")
    txt.printf()
    
    txt.moveCursorLeft()
    txt.printf()
    
    txt.moveCursorLeft()
    txt.printf()
    txt.moveCursorRight()
    
    txt.moveCursorRight()
    txt.moveCursorRight()# doesn't move the cursor because it has reached the right most postion
    txt.printf()
    
    txt.backspace()
    txt.printf()
    txt.backspace()
    txt.printf()
    


    
