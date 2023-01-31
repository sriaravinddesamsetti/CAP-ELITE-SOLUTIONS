# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if root==None:
                return []
            else:
                return trav(root.left)+[root.val]+trav(root.right) 
        res=trav(root)
        s=set(res)
        if len(s)==0 or len(s)==1:
            return -1
        else:
             k=sorted(list(s))
             return k[1]
