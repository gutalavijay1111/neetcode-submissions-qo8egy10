# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = None

        if not list1:
            return list2
        
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                if not result:
                    result = curr1
                    head = result
                else:
                    result.next = curr1
                    result = result.next
                curr1 = curr1.next
            else:
                if not result:
                    result = curr2
                    head = result
                else:
                    result.next = curr2
                    result = result.next

                curr2 = curr2.next
        
        rem = curr1 if not curr2 else curr2

        while rem:
            result.next = rem
            result = result.next
            rem = rem.next

        return head


