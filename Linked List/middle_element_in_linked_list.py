#Finding the middle element of a Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1,2,6,4,5]

head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    current=n1

current=head

while current:
    print(current.data, end="->")
    current=current.next
print("None")

current=head
slow=fast=head

while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
print("Middle element is:",slow.data)

#Finding the middle element of a Doubly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

arr=[1,2,3,4]

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
slow=fast=head

while (fast is not None and fast.next is not None):
    slow=slow.next
    fast=fast.next.next
print()
print("Middle element is:",slow.data)