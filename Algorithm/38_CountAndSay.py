class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
         
        newStr = "1"
        for i in range(1, n):
            curStr = str(newStr)
            newStr = str()
            curDigit = curStr[0]
            curCount = 1
            for j in range(1,len(curStr)):
                if curStr[j] == curDigit:
                    curCount += 1
                else:
                    newStr += str(curCount)
                    newStr += str(curDigit)
                    curDigit = curStr[j]
                    curCount = 1

            newStr += str(curCount)
            newStr += str(curDigit)
        
        return newStr
            
st = Solution()
print st.countAndSay(4)