# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastCurr = head
        slowCurr = head
        if not head.next:
            return False

        while fastCurr.next.next:
            slowCurr = slowCurr.next
            fastCurr = fastCurr.next.next
            if slowCurr == fastCurr:
                return True
            

        return False