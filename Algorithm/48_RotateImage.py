class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if matrix is None or len(matrix) <= 1:
            return matrix
            
        # basically nth column becomes nth row, the sequence of nth row is reversed
        # [r,c] -> [c,(n-1)-r]
        
        newMatrix = list()
        row = 0
        column = 0
        n = len(matrix)
    
        for row in range(0,n):
            newRow = list()
            for column in range(0,n):
                newRow.append(matrix[n-1-column][row])
            newMatrix.append(newRow)
            
        return newMatrix