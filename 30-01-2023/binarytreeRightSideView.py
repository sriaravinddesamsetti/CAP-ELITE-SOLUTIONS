# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res={}
        def rightview(root,res,i):
            if root!=None:
                res[i]=root.val
                rightview(root.right,res,i+1)
                rightview(root.left,res,i+1)
        rightview(root,res,0)
        return res.values()
