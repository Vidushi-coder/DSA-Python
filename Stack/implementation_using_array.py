stack=[]

def push(element):
    stack.append(element)

def pop():
    if isEmpty():
        print("Stack is Empty")
        return None
    else:
        return stack.pop()

def peek():
    if isEmpty():
        print("Stack is Empty")
        return None
    return stack[-1]

def isEmpty():
    if (len(stack)==0):
        return True
    return False

def size():
    return len(stack)

def traverse():
    for i in stack[::-1]:
        print(i,end=" ")

push(1)
push(2)
push(3)
push(4)

print("Stack: ",end="")
traverse()
print("")
print("Popped Element is:",pop())
print("Stack after removal of element: ",end="")
traverse()
print("")
print("Size of the Stack is:",size())
print("Top element of stack is:",peek())