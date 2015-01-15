class Solution:
    # @return a string
    def intToRoman(self, num):
        getVal = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        
        # to save the reverse of all roman characters
        charArray = list()
        index = 0
        curNum = num
        while curNum > 0:
            curStat = 10**index
            curRes = curNum % 10
            curNum = curNum / 10
        
            # check the curRes value , change to Roman character arrays
            curChar = ''
            if curRes in [4,5,9]:
                curChar = getVal[curRes*curStat]
            elif curRes < 5: # add ones/tens/hundreds
                for i in range(1,curRes+1):
                    curChar = curChar + getVal[1*curStat]
            else:#curRes > 5 but < 9
                curChar = curChar + getVal[5*curStat]
                curRes = curRes-5
                for i in range(1,curRes+1):
                    curChar = curChar + getVal[1*curStat]

            charArray.append(curChar)   
            index = index + 1
        
        result = ''
        i = len(charArray) - 1
        while i >= 0 :
            result = result + charArray[i]
            i = i - 1
        
        return result
        