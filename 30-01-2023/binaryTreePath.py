# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        def paths(root,path):
            if root==None:
                return
            path+=str(root.val)+"->"
            if root.left==None and root.right==None:
                l.append(path.rstrip("->"))
            paths(root.left,path)
            paths(root.right,path)
        paths(root,'')
        return l

            


            
