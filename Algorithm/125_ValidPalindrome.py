'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        
        s = s.lower()
        print s
        s = ''.join([ch for ch in s if ch <= 'z' and ch >= 'a' or ch <='9' and ch >= '0'])
        print s

        print s[::-1]
        if s == s[::-1]:
            return True
        else:
            return False
         
