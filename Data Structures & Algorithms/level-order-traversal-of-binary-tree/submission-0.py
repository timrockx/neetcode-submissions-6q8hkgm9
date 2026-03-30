# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []

        if not root:
            return res
        
        # add root into queue
        q.append(root)

        while q:
            # get size of queue (# in current lvl)
            lvl = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            
            res.append(lvl)

        return res



