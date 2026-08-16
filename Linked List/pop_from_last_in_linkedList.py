#Deletion of the last element in a Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1,2,3,4,5]
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

if head is None:
    pass
elif head.next is None:
    head = None
else:
    for i in range(1,len(arr)):
        prev=current
        current=current.next
        if(current.next is None):
            prev.next=None
            break

current=head

while current:
    print(current.data,end="->")
    current=current.next
print("None")

#Deletion of the last element in a Doubly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

arr=[1,2,3,4,5]
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

if head is None:
    pass
elif head.next is None:
    head = None
else:
    current = head
    while current.next:
        prev = current
        current = current.next
    prev.next = None           

current=head

while current:
    print(current.data,end="")
    if(current.next is not None):
        print("<->",end="")
    current=current.next