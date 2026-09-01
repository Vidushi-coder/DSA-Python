from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
    
n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)
n4 = ListNode(9)

n1.next = n2
n2.next = n3
n3.next = n4

x = Solution()
x.deleteNode(n2)

curr = n1
while curr:
    print(curr.val)
    curr = curr.next