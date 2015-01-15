class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if num is None or len(num) == 0:
            return None
        
        if len(num) == 1:
            return num[0]
            
        minIndex = 0
        for i in range(0, len(num)-1):
            if num[i] > num[i+1]:
                minIndex = i+1
           
        return num[minIndex]
        