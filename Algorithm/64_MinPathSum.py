class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0
        
        r, c = len(grid), len(grid[0])
        if r == 0 or c == 0:
            return 0
            
        for i in range(1, c):
            grid[0][i] += grid[0][i-1]
        for i in range(1, r):
            grid[i][0] += grid[i-1][0]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]