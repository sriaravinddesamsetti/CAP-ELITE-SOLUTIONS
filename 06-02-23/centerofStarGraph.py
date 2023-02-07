class Solution:
    def findCenter(self, a: List[List[int]]) -> int:
        if a[0][0] ==a[1][0] or a[0][0]==a[1][1]:
           return a[0][0]
        else:
            return a[0][1]
