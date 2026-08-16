#Reversing a Singly Linked List

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
    current=current.next
print("None")

print("After Reversal:")
current=head
prev=None

while current is not None:
    next_node=current.next
    current.next=prev
    prev=current
    current=next_node

head=prev
current=head

while current:
    print(current.data, end="->")
    current=current.next
print("None")