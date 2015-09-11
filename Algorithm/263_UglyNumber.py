class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
            
        if num == 1:
            return True
        
        div = num
        while div > 10:
            if div%5 == 0:
                div /= 5
                continue
            elif div%3 == 0:
                div /= 3
                continue
            elif div%2 == 0:
                div /= 2
                continue
            else:
                return False
        
        if div == 7:
            return False
            
        return True