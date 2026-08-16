#Implementation of Queue using Array

queue=[]

def push(element):
    queue.append(element)

def pop():
    if isEmpty():
        print("Queue is Empty")
        return None
    else:
        return queue.pop(0)

def peek():
    if isEmpty():
        print("Queue is Empty")
        return None
    else:
        return queue[0]

def isEmpty():
    if(len(queue)==0):
        return True
    return False

def traverse():
    for i in queue:
        print(i,end=" ")

def size():
    return len(queue)

push(1)
push(2)
push(3)
push(4)

print("Queue: ",end="")
traverse()
print("")
print("Popped Element is:",pop())
print("Queue after removal of element: ",end="")
traverse()
print("")
print("Size of the Queue is:",size())
print("Top element of Queue is:",peek())