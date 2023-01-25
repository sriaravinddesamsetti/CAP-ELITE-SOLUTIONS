# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        def height(root):
            if root==None:
                return 0
            lc=height(root.left)
            rc=height(root.right)
            return max(lc,rc)+1
        return max(height(root.left)+height(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
