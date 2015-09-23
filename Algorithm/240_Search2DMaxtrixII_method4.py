class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        targetRows = []
        targetCols = []
        
        for i in range(0 , m):
            if target < matrix[i][0]:
                break
            elif target > matrix[i][-1]:
                continue
            elif target == matrix[i][0] or target == matrix[i][-1]: 
                return True
            else: #target > matrix[i][0] and target < matrix[i][-1]:
                targetRows.append(i)
        
        if len(targetRows) == 0:
            return False
            
        minRow = targetRows[0]
        maxRow = targetRows[-1]
       
        for j in range(0,n):
            if target < matrix[minRow][j]:
                break
            elif target > matrix[maxRow][j]:
                continue
            elif target == matrix[minRow][j] or target == matrix[maxRow][j]: 
                return True
            else: #target > matrix[minRow][j] and target < matrix[maxRow][j]:
                targetCols.append(j)
         
        if len(targetCols) == 0:
            return False
        
        print targetRows
        print targetCols    
        # targetRows and targetColumns are all in ascending order    
        for i in targetRows:
            for j in targetCols:
                if target == matrix[i][j]:
                    return True
        
        return False
            
st = Solution()
a = [[3,6,9,12,17,22],[5,11,11,16,22,26],[10,11,14,16,24,31],[10,15,17,17,29,31],[14,17,20,23,34,37],[19,21,22,28,37,40],[22,22,24,32,37,43]]

print st.searchMatrix(a, 20)