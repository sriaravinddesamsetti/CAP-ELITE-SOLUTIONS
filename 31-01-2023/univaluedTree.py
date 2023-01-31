# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        x=root.val
        def trav(root):
            if root==None:
                return  True
            if root.val!=x:
                return False
            else:
                return trav(root.left) and trav(root.right)
        return trav(root)
