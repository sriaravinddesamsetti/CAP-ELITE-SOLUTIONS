# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res=[]
        def rightview(root,res):
            if root==None:
                return
            if root.left!=None:
                if root.left.left==None and root.left.right==None:
                    res.append(root.left.val)
            rightview(root.left,res)
            rightview(root.right,res)
        rightview(root,res)
        return sum(res)           
