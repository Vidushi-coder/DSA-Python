#Implementation of Stack using Linked List

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size+=1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        popped_node=self.head
        self.head=self.head.next
        self.size-=1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        return self.head.value

    def isEmpty(self):
        return self.size==0
    
    def stackSize(self):
        return self.size
    
    def traverse(self):
        current=self.head
        while current:
            print(current.value,end="->")
            current=current.next
        print()

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
print("Size of the Stack is:",myStack.stackSize())
print("Top element of stack is:",myStack.peek())