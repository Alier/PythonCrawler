'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None or len(words) < 2:
            return 0

        d = []
        words = sorted(words, key=len)
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= (1<< (ord(ch) - 97))
            d.append(mask)

        return max([len(words[i]) * len(words[j]) \
                    for i in xrange(len(d)) for j in xrange(len(d)) \
                    if not d[i] & d[j]] \
                   or [0])
        
            
        
