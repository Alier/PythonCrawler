class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = list()
        result.append([])
        if S is None or len(S) == 0 :
            return result
            
        sortedS = sorted(S)
        for i in range(0, len(sortedS)):
            curDigit = sortedS[i]
            restSets = self.subsets(sortedS[i+1:])
            for st in restSets:
                st.insert(0,curDigit)
                result.append(st)
            
        return result