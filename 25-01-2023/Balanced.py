# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None: 
            return 1
        lc = self.isBalanced(root.left)
        rc=self.isBalanced(root.right)
        if lc == 0 or rc==0: 
            return 0
        if abs(lc - rc) > 1: 
            return 0
        return max(lc, rc) + 1
