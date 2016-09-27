'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1 is None and s2 is None) or len(s1) == 0:
            return True
        
        if s1 is None or s2 is None:
            return False
        
        if len(s1) == 1:
            if s1 == s2:
                return True
            else:
                return False
        
        if sorted(s1) != sorted(s2):
            return False
        
        if len(s2) <= 3:
            return True

        for k in xrange(1, len(s1)):
            if self.isScramble(s1[:k], s2[:k]) and self.isScramble(s1[k:], s2[k:]):
                return True
            if self.isScramble(s1[:k], s2[(-k):]) and self.isScramble(s1[k:], s2[:(-k)]):
                return True
            
        return False
        
