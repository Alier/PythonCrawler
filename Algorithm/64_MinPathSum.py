class Solution(object):
    minSumMatrix = dict()
    
    def minPathSumSub(self, grid, rowStart, columnStart):    	
    	rowEnd = len(grid)-1
    	columnEnd = len(grid[0])-1
    	    	
        m = rowEnd - rowStart + 1
        n = columnEnd - columnStart + 1
        
        if m <= 0 or n <= 0:
            return 0
        
        if m == 1 :
            return sum(grid[rowStart])
        
        result = 0
        if n == 1:
            for i in range(rowStart,rowEnd+1):
                result = result + grid[i][columnStart]
            return result
        
        leftTop = grid[rowStart][columnStart]
       	#print leftTop
       	
        #rightMatrix
        if (rowStart, columnStart+1) in self.minSumMatrix:
            rightMin = self.minSumMatrix[(rowStart, columnStart+1)]
        else:
            rightMin = self.minPathSumSub(grid,rowStart,columnStart+1)
            self.minSumMatrix[(rowStart, columnStart+1)] = rightMin
        #downMatrix
        if (rowStart+1, columnStart) in self.minSumMatrix:
            downMin = self.minSumMatrix[(rowStart+1, columnStart)]
        else:
            downMin = self.minPathSumSub(grid,rowStart+1,columnStart)
            self.minSumMatrix[(rowStart+1, columnStart)] = downMin
        
        #print "rightMin="+str(rightMin)
        #print "downMin="+str(downMin)  
          
        if rightMin < downMin:
            return leftTop + rightMin
        else:
            return leftTop + downMin
        
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) is 0:
            return 0
        
        return self.minPathSumSub(grid, 0, 0)
        
st = Solution()
print st.minPathSum([[0,0],[0,0]])
