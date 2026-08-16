from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = ListNode(0)
        current1=l1
        current2=l2
        current3=sum1
        carry=0
        while(current1 is not None or current2 is not None):
            if current1:
                val1 = current1.val
            else:
                val1 = 0

            if current2:
                val2 = current2.val
            else:
                val2 = 0
                
            total = val1 + val2 + carry
            
            add=total%10
            new_node = ListNode(add)
            
            carry=total//10
            current3.next = new_node

            if current1:
                current1 = current1.next

            if current2:
                current2 = current2.next
                
            current3=current3.next
            
        if carry:
            current3.next = ListNode(carry)
        
        return sum1.next
        
n1 = ListNode(9)
n2 = ListNode(9)
n3 = ListNode(9)
n4 = ListNode(9)
n5 = ListNode(9)
n6 = ListNode(9)
n7 = ListNode(9)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

m1 = ListNode(9)
m2 = ListNode(9)
m3 = ListNode(9)
m4 = ListNode(9)

m1.next = m2
m2.next = m3
m3.next = m4

x = Solution()
result = x.addTwoNumbers(n1,m1)

curr = result
while curr:
    print(curr.val)
    curr = curr.next