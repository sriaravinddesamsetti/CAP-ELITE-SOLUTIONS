# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        def trav(root,i):
            if root==None:
                return
            if i<len(res):
                res[i].append(root.val)
            else:
                res.append([root.val])
            trav(root.left,i+1)
            trav(root.right,i+1)
        trav(root,0)
        f=[]
        for i in res:
            f.append(sum(i)/len(i))
        return f
