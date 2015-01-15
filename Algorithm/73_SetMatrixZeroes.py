class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return
            
        rows = set()
        columns = set()
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
    
        for i in rows:
            for j in range(0,len(matrix[0])):
                matrix[i][j] = 0
        
        for j in columns:
            for i in range(0,len(matrix)):
                matrix[i][j] = 0
                
        return