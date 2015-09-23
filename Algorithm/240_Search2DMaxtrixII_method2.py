class Solution(object):
    def findTarget(self, curRow, target):
        if len(curRow) == 1:
            if target == curRow[0]:
                return True
            return False
        
        if len(curRow) == 2 :
            if target == curRow[0] or target == curRow[1]:
                return True
            return False
        
        midCol = len(curRow)/2
        if target == curRow[midCol]:
            return True
        if target < curRow[midCol]:
            return self.findTarget(curRow[:midCol],target)
        else:
            return self.findTarget(curRow[midCol+1:],target)
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix) # row
        n = len(matrix[0]) #column
        
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        targetRows = []
        for i in range(0,m):
            if i < m-1 and target > matrix[i][-1] and target < matrix[i+1][0]:
                return False
            if i == m-1 and target > matrix[i][-1]:
                return False
            if target < matrix[i][0]  or target > matrix[i][-1]:
                continue
            if target == matrix[i][0] or target == matrix[i][-1]:
                return True
            if target > matrix[i][0]  and target < matrix[i][-1]:
                targetRows.append(i)
        
        for row in targetRows:
            if self.findTarget(matrix[row],target):
                return True
        
        return False
        
st = Solution()
print st.searchMatrix([[1,4],[2,5]],2)