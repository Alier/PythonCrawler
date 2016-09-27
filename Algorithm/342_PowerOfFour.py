'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        if num % 4 > 0:
            return False

        while num/4 > 1 and num % 4 == 0:
            num = num/4

        if num == 4:
            return True
        else:
            return False
