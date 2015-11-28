class Solution(object):
    mapping =[['_'], [], ['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return self.mapping[int(digits[0])]
            
        i = 0
        #print self.mapping[int(digits[i])]
        while i < len(digits) and len(self.mapping[int(digits[i])]) == 0:
            i += 1
       
        print "i="+str(i)
        if i == len(digits): # all "1"s
            return []
        
        result = []
        combFromNext = self.letterCombinations(digits[i+1:])
        if len(combFromNext):
            for comb in combFromNext:
                for curChar in self.mapping[int(digits[i])]:
                    newComb = curChar + str(comb)
                    result.append(newComb)
        
        return result

st = Solution()
print st.letterCombinations("22")