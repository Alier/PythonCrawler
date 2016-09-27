'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) <= 1:
            return 0
    
        idx_stk = list()
        
        for i in xrange(len(s)):
            if s[i] == ')' and len(idx_stk) > 0 and s[idx_stk[-1]] == '(':
                idx_stk.pop()
            else:
                idx_stk.append(i)
        
        if len(idx_stk) == 0:
            return len(s)
        
        idx_stk.append(len(s))
        maxLen = idx_stk[0]
        for j in xrange(len(idx_stk)-1):
            curLen = idx_stk[j+1] - 1 - idx_stk[j]
            if curLen > maxLen:
                maxLen = curLen

        return maxLen
##START = 0
##END = 1
##
##class Solution(object):
##    def longestValidParentheses(self, s):
##        """
##        :type s: str
##        :rtype: int
##        """
##        if s is None or len(s) <= 1:
##            return 0
##    
##        i = 0
##        while i < len(s) and s[i] == ')':
##            i += 1
##        
##        if i >= len(s) - 1: # string is like '))))))' or ')))))('
##            return 0
##        
##        # s[i] == '(' is the first
##        idx_stk = [i]
##        
##        curRanges = list()
##        for j in xrange(i+1, len(s)):
##            if s[j] == '(':
##                idx_stk.append(j)
##            else:  # s[j] == ')'
##                if len(idx_stk) > 0:
##                    curRanges.append((idx_stk.pop(),j))
##
##        print curRanges
##
##        #merge multilayers like:(()) , outer parentheses are later in curRanges
##        i = len(curRanges) - 1
##        while i > 0:
##            if curRanges[i-1][START] > curRanges[i][START] and \
##               curRanges[i-1][END] < curRanges[i][END]:
##                 del curRanges[i-1]
##            i -= 1
##        print curRanges
##        
##        #merge consequtive ranges like ()()
##        i = 0
##        while i < len(curRanges) - 1:
##            if curRanges[i][END]+1 == curRanges[i+1][START]:
##                curRanges[i] = (curRanges[i][START], curRanges[i+1][END])
##                del curRanges[i+1]
##                i -= 1
##            i += 1
##    
##        print curRanges
##
##        #calculate maxLen
##        maxLen = 0
##        for start, end in curRanges:
##            curLen = end-start+1
##            if curLen > maxLen:
##                maxLen = curLen
##
##        return maxLen
