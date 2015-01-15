class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        baseTriangle = [[1],[1,1]]
        
        if rowIndex <= 1:
            return baseTriangle[rowIndex]
        
        lastRow = self.getRow(rowIndex-1)
        print lastRow
        thisRow = list()
        thisRow.append(1)
        for i in range(1,rowIndex):
            thisRow.append(lastRow[i-1]+lastRow[i])
        thisRow.append(1)
    
        return thisRow

st = Solution()
print st.getRow(2)
