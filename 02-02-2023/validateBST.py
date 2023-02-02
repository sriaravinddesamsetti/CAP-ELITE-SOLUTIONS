# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if root== None:
                return []
            else:
                return inorder(root.left)+[root.val]+inorder(root.right)
        k=inorder(root)
        if k==sorted(list(set(k))):
            return True
        else:
            return False
