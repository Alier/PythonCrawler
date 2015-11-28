class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        curStr = strs[0]
        for i in range(0, len(curStr)):
            curChar = curStr[i]
            #check whether curChar in other string same position
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != curStr[i]:
                    return curStr[0:i]
            
        return curStr    
            