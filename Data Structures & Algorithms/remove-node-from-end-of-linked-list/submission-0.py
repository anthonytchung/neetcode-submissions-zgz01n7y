# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr2 = curr = head
        N = 0

        while curr:
            N += 1
            curr = curr.next
        
        removal = N - n

        if removal == 0:
            head = head.next
            return head
        
        for i in range(N):
            if i == removal-1:
                curr2.next = curr2.next.next
                break
            curr2 = curr2.next
        return head
            