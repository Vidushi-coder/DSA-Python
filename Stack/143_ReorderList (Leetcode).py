# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        stack = []

        current = head
        while current:
            stack.append(current)
            current = current.next

        current = head
        n = len(stack)

        for i in range(n // 2):

            nextNode = current.next      

            last = stack.pop()           

            current.next = last         
            last.next = nextNode        
            
            current = nextNode           

        current.next = None 
        
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

x = Solution()
x.reorderList(n1)

curr = n1
while curr:
    print(curr.val)
    curr = curr.next

# optimal approach

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return

        # Step 1: Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        current = slow.next
        slow.next = None

        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Merge
        first = head
        second = prev

        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2
        
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

x = Solution()
x.reorderList(n1)

curr = n1
while curr:
    print(curr.val)
    curr = curr.next