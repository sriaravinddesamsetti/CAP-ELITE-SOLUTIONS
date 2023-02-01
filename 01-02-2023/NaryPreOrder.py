"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l=[]
        if root==None:
            return []
        for i in root.children:
            l+=self.preorder(i)
        return [root.val]+l
