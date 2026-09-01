#Deleting from the front of a Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[5,1,2,3,4]
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

print("After deletion:")

if(head is not None):
    head=head.next
current=head

while current:
    print(current.data,end="->")
    current=current.next
print("None")

#Deleting from the front of a Doubly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

arr=[5,1,2,3,4]
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

print()
print("After deletion:")

if(head is not None):
    head=head.next
    if (head is not None):
        head.prev=None
current=head

while current:
    print(current.data,end="")
    if(current.next is not None):
        print("<->",end="")
    current=current.next