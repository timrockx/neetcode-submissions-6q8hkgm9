# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """        
        tree = []
        def inorder(root):
            if not root:
                return             
            inorder(root.left)
            tree.append(root)
            inorder(root.right)
        
        inorder(root)

        i, n = 0, len(tree)
        node1, node2 = None, None
        
        while i < n and i+1 < n:
            if tree[i].val > tree[i+1].val:
                if not node1:
                    node1 = tree[i]
                node2 = tree[i+1]
            i += 1
        
        node1.val, node2.val = node2.val, node1.val