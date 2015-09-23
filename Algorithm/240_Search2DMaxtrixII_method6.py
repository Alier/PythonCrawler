class Solution(object):
    def searchSubMatrix(self, matrix, rowStart, rowEnd, colStart, colEnd, target):
    	#print "rowStart/rowEnd ="+str(rowStart)+"/"+str(rowEnd)
    	#print "colStart/colEnd ="+str(colStart)+"/"+str(colEnd)
		
        if rowStart == rowEnd and colStart == colEnd: # only one element might fit
            if matrix[rowStart][colStart] == target:
                return True
            return False
        
        if target < matrix[rowStart][colStart] or target > matrix[rowEnd][colEnd]:
            return False
            
        if rowStart == rowEnd:    # colStart < colEnd only one row
            for j in range(colStart, colEnd+1):
                if target == matrix[rowStart][j]:
                    return True
            return False
        
        if colStart == colEnd:   # only one colomn
            for i in range(rowStart,rowEnd+1):
                if target == matrix[i][colStart]:
                    return True
            return False
            
        # column and row both >= 2
        newRowStart = -1
        newRowEnd = rowEnd
        
        for i in range(rowStart, rowEnd + 1) :
            if target == matrix[i][colStart] or target == matrix[i][colEnd]:
                return True
            if target > matrix[i][colEnd]:
                continue
            if target < matrix[i][colStart]:
                newRowEnd = i - 1
                break
            else: # target > matrix[i][0] and target < matrix[i][-1]:
                if newRowStart < 0:
                    newRowStart = i
               
        if newRowStart < 0:
            return False
        
        newColStart = -1
        newColEnd = colEnd
        
        for j in range(colStart, colEnd + 1):
            if target == matrix[newRowStart][j]  or target == matrix[newRowEnd][j]:
                return True
            if target > matrix[newRowEnd][j]:
                continue
            if target < matrix[newRowStart][j]:
                newColEnd = j - 1
                break
            else: #target > matrix[startRow][j] and target < matrix[endRow][j]:
                if newColStart < 0:
                    newColStart = j
               
        if newColStart < 0:
            return False
        
        #if self.count >= 0:
        #	self.count -= 1
        return self.searchSubMatrix(matrix, newRowStart, newRowEnd, newColStart, newColEnd, target)
        #return False
            
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        return self.searchSubMatrix(matrix, 0, m-1, 0, n-1, target)
    
    #count = 5
    
st = Solution()
a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print st.searchMatrix(a,20)