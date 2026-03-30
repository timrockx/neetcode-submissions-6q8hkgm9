"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        cur = head
        res = dummy = Node(0, None, None)
        mp = {}
        i = 0

        while cur:
            res.next = Node(cur.val, None, None)
            res = res.next
            mp[cur] = res            
            cur = cur.next

        cur, res = head, dummy.next
        while cur:
            if cur.random is not None:
                res.random = mp[cur.random]
            else:
                res.random = None

            cur = cur.next
            res = res.next

        return dummy.next


