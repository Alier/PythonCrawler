class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    known = {}
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        
        # if end point is already blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        return self.uniquePathsInGrid(obstacleGrid, 0, 0)
        
    def uniquePathsInGrid(self, obstacleGrid, startRow, startColumn):
        if (startRow,startColumn) in self.known:
            return self.known[(startRow,startColumn)]
        
        result = 0
        
        # starting point is 1 already
        if obstacleGrid[startRow][startColumn] == 1:
            self.known[(startRow,startColumn)] = 0
            return 0
            
        lastRow = len(obstacleGrid) - 1
        lastColumn = len(obstacleGrid[0]) - 1
        
        # end point
        if startRow == lastRow and startColumn == lastColumn:
            self.known[(startRow,startColumn)] = 1
            return 1
        
        #only one row, check if there is 1 in the row
        if startRow == lastRow and startColumn < lastColumn:
            if 1 in obstacleGrid[startRow][startColumn:]:
                result = 0
            else:
                result = 1
            self.known[(startRow,startColumn)] = result
            return result
            
        #only one column, check if there is 1 in the column
        if startRow < lastRow and startColumn == lastColumn:
            for i in range (startRow,lastRow+1):
                if obstacleGrid[i][startColumn] == 1:
                    result = 0
                    break
            if i == lastRow :
                result = 1
            self.known[(startRow,startColumn)] = result
            return result
            
        # more than one column and one row, recursive call
        # able to go down
        result = self.uniquePathsInGrid(obstacleGrid, startRow + 1, startColumn) + self.uniquePathsInGrid(obstacleGrid, startRow, startColumn + 1)
        
        self.known[(startRow,startColumn)] = result
        return result

st = Solution()
A = [[0,0],[0,0]]
print st.uniquePathsWithObstacles(A)
