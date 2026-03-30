# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        curr = 0
        def dfs(root):
            nonlocal curr

            if not root:
                return

            if low <= root.val <= high:
                curr += root.val
                if root.val > low:
                    dfs(root.left)
                if root.val < high:
                    dfs(root.right)

            if root.val < low:
                dfs(root.right)
            if root.val > high:
                dfs(root.left)
            
        dfs(root)
        return curr