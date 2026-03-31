# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first, second = head, head

        while n:
            second = second.next
            n -= 1
        
        prev = None
        while second:
            second = second.next
            prev = first
            first = first.next

        if not prev:
            return head.next
            
        prev.next = first.next
        first.next = None

        return head

        