#Deletion from the middle of a Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1,2,5,3,4]
head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    current=n1

current=head

while current:
    print(current.data,end="->")
    current=current.next
print("None")

current=head
print("After Deletion:")

for i in range(1,len(arr)):
    prev=current
    current=current.next
    if(current.data==5):
        prev.next=current.next
        break

current=head

while current:
    print(current.data,end="->")
    current=current.next
print("None")

#Deletion from the middle of a Doubly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

arr=[1,2,5,3,4]
head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    n1.prev=current
    current=n1

current=head

while current:
    print(current.data,end="")
    if(current.next is not None):
        print("<->",end="")
    current=current.next

current=head
print()
print("After Deletion:")

for i in range(1,len(arr)):
    prev=current
    current=current.next
    if(current.data==5):
        prev.next=current.next
        current.next.prev=prev
        break

current=head

while current:
    print(current.data,end="")
    if(current.next is not None):
        print("<->",end="")
    current=current.next