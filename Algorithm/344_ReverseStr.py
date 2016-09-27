'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return s

        chs = list(s)
        revChs = [chs[len(chs)-1-i] for i in xrange(0, len(chs))]

        return ''.join(revChs)    
