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

head=n1
current = head

while current:
    print(current.data, end="->")
    current=current.next
print("None")

#OR
print()

arr=[1,2,3,4,5]

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