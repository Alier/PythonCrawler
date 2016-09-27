'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution(object):
    
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counts = [0,1,1] + [None] * (num+1-3)

        if num < 3:
            return counts[:num+1]
        
        for n in xrange(3, num+1):
            a, b = divmod(n, 2)
            counts[n] = counts[a] + b

        return counts