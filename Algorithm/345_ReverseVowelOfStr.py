'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''

VOWELS = 'aeiouAEIOU'

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return s

        indexes = []
        for i in xrange(0, len(s)):
            if s[i] in VOWELS:
                indexes.append(i)
                            
        if len(indexes) <= 1:
            return s
        
    
        i = 0
        j = len(indexes) - 1
        chs = list(s)
        while i < j:
            idx1 = indexes[i]
            idx2 = indexes[j]
            # exchange chs[idx1] and chs[idx2]
            temp = chs[idx1]
            chs[idx1] = chs[idx2]
            chs[idx2] = temp
            i += 1
            j -= 1
            
        return ''.join(chs)
    
