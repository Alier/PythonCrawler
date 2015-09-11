class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        highest = 0
        missing = []
        
        for num in nums:
           if num <= 0:
               continue
           if num > highest:
               for x in range(highest+1,num):
                   missing.append(x)
               highest = num
           elif num == highest:
               continue
           else : # num < highest
               if num in missing:
                   missing.remove(num)
    
        if len(missing) > 0:
            return missing[0]
        else:
            return highest+1
        