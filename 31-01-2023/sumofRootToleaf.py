# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=[]
        def trav(root,s):
            if root==None:
                return
            s+=str(root.val)
            if root.left==None and root.right==None:
                res.append(int(s,2))
            trav(root.left,s)
            trav(root.right,s)
        trav(root,'')
        print(res)
        return sum(res)
