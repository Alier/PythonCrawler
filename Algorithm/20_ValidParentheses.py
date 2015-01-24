class Solution:
    # @return a boolean
    def isValid(self, s):
        if s is None or len(s) == 0:
            return True
        
        if len(s) % 2 > 0:
            return False
        
        pairs = {'(':')','[':']','{':'}'}
        stk = list()
        for ch in s:
            if ch in pairs: #left brackets, just push into stack
                stk.append(ch)
            else: # ch in rights
                if len(stk) == 0:
                    return False
                lastCh = stk.pop()
                needed = pairs[lastCh]
                if ch != needed:
                    return False
        
        if len(stk) > 0:
            return False
        return True