class Solution:
    # @return an integer
    def romanToInt(self, s):
        getVal = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        if len(s) == 0:
            return 0
            
        if len(s) == 1:
            return getVal[s]
        
        i = len(s)-1 #from last to first
        result = 0
        
        while i > 0:
            j = i - 1 # j is pointing to the character to the left of i's
            curVal = getVal[s[i]]
            leftVal = getVal[s[j]]
            
            # if left is larger than right, right + left
            if leftVal >= curVal:
                result = result + curVal
                i = i - 1
            else: # left is smaller, find pattern
                result = result + getVal[s[j:i+1]]
                i = i - 2
    
        if i == 0:
            result = result + getVal[s[i]]
        
        return result