# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        in_left = self.lowestCommonAncestor(root.left, p, q)
        in_right = self.lowestCommonAncestor(root.right, p, q)

        if in_left and in_right:
            return root

        return in_left if in_left else in_right