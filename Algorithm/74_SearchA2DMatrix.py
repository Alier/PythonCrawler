class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        # if not possibly in the matrix
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for i in range(0,m-1): #find row first
            if target >= matrix[i][0] and target < matrix[i+1][0]: #in row i possibly
                if target > matrix[i][-1]:
                    return False
                #search in this row
                for j in range(0,n):
                    if matrix[i][j] == target:
                        return True
                
        # check if in last row, i == m-2
        for j in range(0,n):
            if matrix[-1][j] == target:
                    return True
                    
        return False