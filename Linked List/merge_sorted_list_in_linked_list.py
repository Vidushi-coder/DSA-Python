#Merging two sorted Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1,2,4]

head=Node(arr[0])
current=head

for i in range(1,len(arr)):
    n1=Node(arr[i])
    current.next=n1
    current=n1

current=head

arr1=[3,4,5]

head1=Node(arr1[0])
current1=head1

for i in range(1,len(arr1)):
    n1=Node(arr1[i])
    current1.next=n1
    current1=n1

current1=head1

p1=head
p2=head1  

if p1.data<=p2.data:
    merged_head=p1
    p1=p1.next
else:
    merged_head=p2
    p2=p2.next
tail=merged_head

while p1 and p2:
    if p1.data<=p2.data:
        tail.next=p1
        p1=p1.next
    else:
        tail.next=p2
        p2=p2.next
    tail=tail.next

if p1:
    tail.next = p1
else:
    tail.next = p2

current = merged_head

while current:
    print(current.data, end="->")
    current = current.next

print("None")