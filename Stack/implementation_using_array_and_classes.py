#Implementing stack using Array and Classes

class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            return self.stack[-1]

    def isEmpty(self):
        if (len(self.stack)==0):
            return True
        return False
    
    def size(self):
        return len(self.stack)
    
    def traverse(self):
        for i in self.stack[::-1]:
            print(i,end=" ")

myStack=Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)

print("Stack: ",end="")
myStack.traverse()
print("")
print("Popped Element is:",myStack.pop())
print("Stack after removal of element: ",end="")
myStack.traverse()
print("")
print("Size of the Stack is:",myStack.size())
print("Top element of stack is:",myStack.peek())