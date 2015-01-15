class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 0 or num is None:
            return None
            
        if len(num) == 1:
            return num[0]
            
        #unless there is sudden descending, the first one is the min
        for i in range(0,len(num)-1):
            if num[i] > num[i+1]:
                return num[i+1]

        return num[0]