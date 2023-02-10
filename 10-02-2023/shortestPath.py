class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q=[[0,0,1]]
        if grid[0][0]==1:
            return -1
        while q:
            x,y,steps=q.pop(0)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return steps 
            for i,j in [[x+1,y+1],[x-1,y-1],[x+1,y-1],[x-1,y+1],[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==0:
                    grid[i][j]='/'
                    q.append([i,j,steps+1])
        return -1      

        
