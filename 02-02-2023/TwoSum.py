# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], v: int) -> bool:
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        k=inorder(root)
        for i in range(len(k)):
            for j in range(i+1,len(k)):
                if k[i]+k[j]==v:
                    return True
                    break
        return False
