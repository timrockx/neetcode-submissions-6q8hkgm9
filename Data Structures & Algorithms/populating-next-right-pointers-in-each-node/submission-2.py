"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        q = deque()
        q.append(root)

        while q:
            n = len(q)
            lvl = []
            for i in range(n):
                node = q.popleft()
                lvl.append(node)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            for i in range(n-1):
                if i+1 < n:
                    lvl[i].next = lvl[i+1]
                else:
                    lvl[i].next = None
        
        return root

