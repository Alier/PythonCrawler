class Solution(object):
    def findRows(self, matrix, target): # matrix has at least one row and one column
        m = len(matrix) # row
        n = len(matrix[0]) #column
        
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return []
        
        if m == 1: # only one row
            return [0]
        
        targetRows = [] 
        
        if m == 2: # only two rows
        	if target > matrix[0][-1] and target < matrix[1][0]:
        		return []
        	if target >= matrix[0][0] and target <= matrix[0][-1]:
        		targetRows.append(0)
        	if target >= matrix[1][0] and target <= matrix[1][-1]:
        		targetRows.append(1)
        	return targetRows
            
        # m >= 3:
        midRow = m/2
        if target > matrix[midRow][-1]: # larger than end of midRow
            subRows = self.findRows(matrix[midRow+1:],target)
            if len(subRows):
                for row in subRows:
                    targetRows.append(row+midRow+1)
            return targetRows
       
        if target < matrix[midRow][0]: # smaller than starting of midRow
            subRows = self.findRows(matrix[:midRow],target)    
            if len(subRows):
                for row in subRows:
                    targetRows.append(row)
            return targetRows
            
        # target <= matrix[midRow][-1] and target >= matrix[midRow][0], in midRow, search up and down from midRow
        r = midRow
        while r < m and target <= matrix[r][-1] and target >= matrix[r][0]:
            targetRows.append(r)
            r += 1
        
        r = midRow
        while r >= 0 and target <= matrix[r][-1] and target >= matrix[r][0]:
            targetRows.append(r)
            r -= 1
        
        return targetRows
            
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
        
        targetRows = self.findRows(matrix,target)
        if len(targetRows) == 0:
            return False
            
        #print targetRows
        for row in targetRows:
            if self.findTarget(matrix[row],target):
                return True
        
        return False
        
st = Solution()
print st.searchMatrix([[48,65,70,113,133,163,170,216,298,389],[89,169,215,222,250,348,379,426,469,554],[178,202,253,294,367,392,428,434,499,651],[257,276,284,332,380,470,516,561,657,698],[275,331,391,432,500,595,602,673,758,783],[357,365,412,450,556,642,690,752,801,887],[359,451,534,609,654,662,693,766,803,964],[390,484,614,669,684,711,767,804,857,1055],[400,515,683,732,812,834,880,930,1012,1130],[480,538,695,751,864,939,966,1027,1089,1224]], 802)