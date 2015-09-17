class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1 :
            return False
        
        count = 0
        while n > 0: 
        	print n
        	if n & 1 == 1: 
        		count += 1
        		print "count = "+str(count)
    		n = n >> 1
        
        if count != 1:
            return False
        else:
            return True
            
st = Solution()
print st.isPowerOfTwo(16777216)#33554432) #16777216