# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def trav(root,i):
            if root==None:
                return []
            if i<len(res):
                res[i].append(root.val)
            else:
                res.append([root.val])
            trav(root.left,i+1)
            trav(root.right,i+1)
        trav(root,0)
        return res
