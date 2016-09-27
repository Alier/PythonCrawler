'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None or len(haystack) < len(needle):
            return -1
         
        if len(needle) == 0 and len(haystack) >= 0:
            return 0
            
        possibleHead = [x for x in xrange(len(haystack)) if haystack[x] == needle[0]]
        for head in possibleHead:
            if len(haystack[head:]) < len(needle):
                return -1
            if haystack[head:head+len(needle)] == needle:
                return head
        
        return -1

           
