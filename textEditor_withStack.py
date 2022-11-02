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
from Stack_with_linkedList import *
class TextEditor:
    def __init__(self):

        self.UNDO = Stack()
        self.REDO = Stack()
        

    def write(self, data): # adds charachters 

        self.UNDO.push(data)

    def backspace(self): # deletes elements
        
        data = self.UNDO.pop()
        self.REDO.push(data)

    def undo(self): # undo operation
        data = self.UNDO.peek()
        self.UNDO.pop()
        self.REDO.push(data)
        
    def redo(self): # redo operation
        data = self.REDO.peek()
        self.REDO.pop()
        self.UNDO.push(self.REDO.pop())
        
    

    def printf(self): #prints the reversed stack

        result = ""
        for i in range(self.UNDO.length()):
            result += " " + str(self.UNDO.pop())    
        result = result[: -3]
        
        result = result[::-1] 
        print(result)
    

if __name__ == '__main__':

    txt = TextEditor()
    txt.write("N")
    txt.printf()
    
    txt.write("M")
    txt.write("k")
    
    txt.undo()
    txt.printf()
    txt.backspace()
    txt.printf()
   
    
    
