# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        rt_index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:rt_index + 1], inorder[0:rt_index])
        root.right = self.buildTree(preorder[rt_index+1:len(preorder)], inorder[rt_index+1:len(inorder)])
        
        return root