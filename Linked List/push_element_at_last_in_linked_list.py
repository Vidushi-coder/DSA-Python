#Inserting at the last of a Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1,2,3,4]
head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    current=n1

current=head
new_node=Node(5)
while current.next is not None:
    current=current.next

current.next=new_node

current=head

while current:
    print(current.data,end="->")
    current=current.next
print("None")

#Inserting at the last of a Doubly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

arr=[1,2,3,4]
head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    n1.prev=current
    current=n1

current=head
new_node=Node(5)

while current.next is not None:
    current=current.next
current.next=new_node
new_node.prev=current

current=head

while current:
    print(current.data,end="")
    if(current.next is not None):
        print("<->",end="")
    current=current.next