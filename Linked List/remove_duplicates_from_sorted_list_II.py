from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        current = head
            
        while(current is not None and current.next is not None):
            if(current.val == current.next.val):
                while(current.next is not None and current.val == current.next.val) :
                    current = current.next
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next

            
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