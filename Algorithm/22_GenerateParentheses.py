class Solution:
    known = {1:['()'],2:['(())','()()']}
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n is None or n == 0 :
            return None
        
        if n in self.known:
            return self.known[n]

        self.known[n] = self.getMergedSet(self.generateParenthesis(n-1))
        return self.known[n]
        
    def getMergedSet(self, origSet):
        newList = list()
        for pattern in origSet:
            insertedList = self.getInsertedPattern(pattern)
            for str in insertedList:
                if str not in newList:
                    newList.append(str)
                    
        return newList
        
    # for pattern (()()), insert another () into this pattern, should get :
    # ((i)()()), (((i))()),(()((i))), basiclaly insert after each '(', return a list
    def getInsertedPattern(self,origStr):
        result = list()
        for i in range(0,len(origStr)):
            if origStr[i] == '(':
                result.append(origStr[0:i+1]+"()"+origStr[i+1:])
        result.append(origStr+"()")
        result.append("()"+origStr)
        return result