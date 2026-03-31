"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:    
    ll_map = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None

        if head in self.ll_map:
            return self.ll_map[head]

        new_head = Node(head.val)
        self.ll_map[head] = new_head
        new_head.next = self.copyRandomList(head.next)
        new_head.random = self.ll_map.get(head.random)
        return new_head
