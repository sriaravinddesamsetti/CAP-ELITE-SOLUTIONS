"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l=[]
        if root==None:
            return []
        for i in root.children:
            l+=self.postorder(i)
        return l+[root.val]
