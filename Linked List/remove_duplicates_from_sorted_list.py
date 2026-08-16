from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
            
        while(current is not None and current.next is not None):
            if(current.val == current.next.val) :
                current.next=current.next.next
            else:
                current = current.next
        
        return head

            
n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)



n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

x = Solution()
result = x.deleteDuplicates(n1)

curr = result
while curr:
    print(curr.val)
    curr = curr.next