# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(root, curr_max):
            nonlocal res

            if not root:
                return 0

            if root.val >= curr_max:
                res += 1
                curr_max = root.val
            
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)

        dfs(root, float('-inf'))
        return res