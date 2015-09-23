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
        startRow = -1 
        endRow = m-1
       
        for i in range(0,m) :
            if target == matrix[i][0] or target == matrix[i][-1]:
                return True
            if target > matrix[i][-1]:
                continue
            if target < matrix[i][0]:
                endRow = i - 1
                break
            else: # target > matrix[i][0] and target < matrix[i][-1]:
                if startRow < 0:
                    startRow = i
                else:
                    continue
        
        if startRow < 0:
            return False
        
        newMatrix = matrix[startRow:endRow+1]
        if startRow == endRow : #only one row
            for j in range(0,len(newMatrix[0])):
                if target == newMatrix[0][j]:
                    return True
            return False
        
        n = len(newMatrix[0])
        startCol = -1
        endCol = n-1
        
        print newMatrix
        for j in range(0, n):
        	print j
        	print endRow
        	minElemInCol = newMatrix[0][j] 
        	maxElemInCol = newMatrix[-1][j]
        	
        	if target == newMatrix[0][j]  or target == newMatrix[-1][j]:
        		return True
        	if target > newMatrix[-1][j]:
        		continue
        	if target < newMatrix[0][j]:
        		endCol = j - 1
        		break
        	else: #target > matrix[startRow][j] and target < matrix[endRow][j]:
        		if startCol < 0:
        			startCol = j
        		else:
        			continue
            
        if startCol < 0:
            return False
        
        retMatrix = []
        for row in newMatrix:
            retMatrix.append(row[startCol:endCol+1])
        
        if startCol == endCol: #only one column
            for i in range(0,len(retMatrix)):
                if target == retMatrix[i][0]:
                    return True
            return False
                
        return self.searchMatrix(retMatrix,target)
        
st = Solution()
a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print st.searchMatrix(a,20)