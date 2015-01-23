class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        div = 5
        result = 0
        while div <= n:
            result += n//div
            if div > (0x7FFFFFFF/5):
                break
            div = div*5
            print "result = "+ str(result) +" div = "+str(div)
        return result

    def getResult(self,n):
        result = 1
        for i in range(1,n+1):
            result = result * i

        return result

st = Solution()
print st.getResult(25)
print st.trailingZeroes(25)
