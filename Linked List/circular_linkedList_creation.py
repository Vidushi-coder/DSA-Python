#singly linked list

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
current=head

while current:
    print(current.data,end="->")
    current=current.next
    if current==head:
        break
print(current.data)

#OR
print()

arr=[1,2,3,4]

head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    current=n1

current.next=head

current=head

while current:
    print(current.data,end="->")
    current=current.next
    if current==head:
        break
print(current.data)

#doubly linked list
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n1
n1.prev=n4
n2.prev=n1
n3.prev=n2
n4.prev=n3

head=n1
current=head

while current:
    print(current.data,end="<->")
    current=current.next
    if current==head:
        break
print(current.data)

#OR
print()

arr=[1,2,3,4]

head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    n1.prev=current
    current=n1

current.next=head
current=head

while current:
    print(current.data,end="<->")
    current=current.next
    if current==head:
        break
print(current.data)