#Implementation of Queue using Linked List

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def enqueue(self,value):
        new_node=Node(value)

        if (self.head is None):
            self.tail=new_node
            self.head=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

        self.size+=1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        if self.head is None:
            self.tail = None
        else:
            popped_element=self.head
            self.head=self.head.next
            self.size-=1
            return popped_element.value
        
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            return self.head.value

    def isEmpty(self):
        return self.size==0
    
    def queueSize(self):
        return self.size
    
    def traverse(self):
        current=self.head
        while current:
            print(current.value,end="->")
            current=current.next
        print()

myQueue=Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)

print("Queue: ",end="")
myQueue.traverse()
print("")
print("Popped Element is:",myQueue.dequeue())
print("Queue after removal of element: ",end="")
myQueue.traverse()
print("")
print("Size of the Queue is:",myQueue.queueSize())
print("Top element of Queie is:",myQueue.peek())