class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        peakIndex = 0
        
        if num is None or len(num) == 0:
            return None
            
        if len(num) == 1:
            return peakIndex
            
        i = 0
        while i < len(num)-1:
            if num[i] < num[i+1]:
                peakIndex = i + 1
                i = i + 1
            else:
                return peakIndex
        
        return peakIndex