def numIslands(grid):
        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            dfs(grid,i-1,j-1)
            dfs(grid,i-1,j+1)
            dfs(grid,i+1,j-1)
            dfs(grid,i+1,j+1)
        if len(grid)==0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    count += 1
        return count
n=[int(x) for x in input().split()]
grid=[list(map(int,input().split())) for i in range(n[0])]
print(numIslands(grid))
