class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s is None or len(s) == 0:
            return 0
        
        startOfWord = -1
        endOfWord = len(s) 
        wordFlag = False
        for i in range(0,len(s)):
            if s[i] != ' ' and wordFlag is False:
                startOfWord = i
                wordFlag = True
            elif s[i] == ' ' and wordFlag is True:
                endOfWord = i
                wordFlag = False
        
        if startOfWord == -1:
            return 0
            
        # no space in the end
        if wordFlag is True:
            endOfWord = len(s)
        
        return len(s[startOfWord:endOfWord])

st = Solution()
print st.lengthOfLastWord("a ")
