#Length of a Singly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1,2,3,4,5]
cnt=0

head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    current=n1

current=head

while current:
    print(current.data, end="->")
    cnt+=1
    current=current.next
print("None")

print("Length of the Linked List is:",cnt)

#Length of a Doubly Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

arr=[1,2,3,4]
cnt=0

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
    cnt+=1
    if(current.next is not None):
        print("<->",end="")
    current=current.next

print()
print("Length of the Linked List is:",cnt)