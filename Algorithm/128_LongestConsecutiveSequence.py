class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if num is None:
            return 0
        
        totalCount = len(num)
        if totalCount <= 1:
            return totalCount
        
        sortedNum = sorted(num)
        print sortedNum
        result = 1
        maxResult = 0
        for i in range(0,totalCount-1):
            if sortedNum[i+1] == sortedNum[i] + 1:
                result = result + 1
            elif sortedNum[i+1] == sortedNum[i]:
                continue
            else: # breaks. reset result
                if result > maxResult:
                    maxResult = result
                result = 1
              
        if result > maxResult:
            maxResult = result
        
        return maxResult

st = Solution()
print st.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
