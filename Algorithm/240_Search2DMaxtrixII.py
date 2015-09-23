class Solution(object):
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
        
        for i in range(0,m):
            if target < matrix[i][0]: 
                return False
            if target > matrix[i][-1]:
                continue
            else: # might in this row, step
                for j in range(0,n): # first and last digit already checked in previous step
                    if matrix[i][j] == target:
                        return True
                    if matrix[i][j] > target:
                        break;
        
        
        if i == m-1:
            return False
            
st = Solution()
print st.searchMatrix([[-1,0,3],[-1,0,1],[0,1,3]],2)