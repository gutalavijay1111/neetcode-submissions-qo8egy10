# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        # reverse second half links (save mid pointer)
        # merge both halves.

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # joining the reversed seconf half, with the first half
        # mid.next = prev
        # I dont think this is needed, we can simply consider the prev as start of second half

        # merge first and second half.

        curr1, curr2 = head, prev
        while curr1 and curr2:
            curr1_nxt = curr1.next
            curr1.next = curr2
            curr2_nxt = curr2.next
            curr2.next = curr1_nxt
            curr1, curr2 = curr1_nxt, curr2_nxt


        curr = head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
