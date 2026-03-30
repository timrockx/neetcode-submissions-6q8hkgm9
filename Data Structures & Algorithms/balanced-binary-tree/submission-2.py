# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root) -> int:
            if not root:
                return -1

            if not root.left and not root.right:
                return 0
            
            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return True

        l_height = height(root.left)
        r_height = height(root.right)

        if abs(l_height - r_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        

        
