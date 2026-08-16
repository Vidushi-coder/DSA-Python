#Detecting cycle in Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n1

head=n1
current=n1

while current:
    print(current.data,end="->")
    current=current.next
    if current==head:
        break
print(current.data)

slow=fast=head

while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow == fast:
        cycle = True
        break

if cycle:
    print("Cycle exists")
else:
    print("No cycle")