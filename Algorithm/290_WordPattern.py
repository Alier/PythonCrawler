class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern is None or len(pattern) == 0 or str is None or len(str) == 0:
            return False
        
        strList = str.split(" ")
        if len(pattern) == 1 and len(strList) == 1:
            return True
        
        if len(pattern) > len(strList):
            return False
            
        mappingPatternToStr = {}
        mappingStrToPattern = {}
        for i in range(0,len(pattern)):
            print mappingPatternToStr
            print mappingStrToPattern
            if pattern[i] in mappingPatternToStr:
                expectedStr = mappingPatternToStr[pattern[i]]
                if strList[i] != expectedStr:
                    return False
            elif strList[i] in mappingStrToPattern:
                expectedPattern = mappingStrToPattern[strList[i]]
                if pattern[i] != expectedPattern:
                    return False
            else:
                mappingPatternToStr[pattern[i]] = strList[i]
                mappingStrToPattern[strList[i]] = pattern[i]
        
        return True
            
st = Solution()
print st.wordPattern("abba","dog cat cat dog")