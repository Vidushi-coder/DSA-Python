#Implementing queue using Array and Classes

class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return (len(self.queue)==0)
    
    def traverse(self):
        for i in self.queue:
            print(i,end=" ")
    
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
print("Size of the Queue is:",myQueue.size())
print("Top element of queue is:",myQueue.peek())