import sys
pow3 = [pow(3,x) for x in xrange(10)]

class Solution(object):
    '''
    Given an integer, write a function to determine if it is a power of three.
    '''
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
            
        if n%3 != 0 and n != 1:
            return False
        
        if n in pow3:
            return True
            
        return n%pow3[-1] == 0 and self.isPowerOfThree(n/pow3[-1])


if __name__ == '__main__':
    st = Solution()
    print st.isPowerOfThree(int(sys.argv[1]))
