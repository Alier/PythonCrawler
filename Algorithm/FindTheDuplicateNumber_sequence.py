# this solution only works if there is no middle number missing in the sequence
# if the repeated number repeated (2n+1) times after its normal appearance, like [1,2,3,3,3,3], x =^ array = ^[1,2] 
# y = ^[smallest, smallest+1,.... largest], in this case y = ^[1,2,3], then x != y, and result = x ^ y
# if repeated number repeated 2n times after its normal appearance, like [1,2,3,3,3], then x = ^ array = ^[1,2,3]
# y = ^[1,2,3], x == y, can't get result as above. We need to try x1 = sum(array) = 1+2+3X3, y1 = sum(lowest to largest) = 1+2+3
# according to x1 - y1 = resultNumber * extraDupTime , 
# calculate range of extaDupTime: n = len(array) in this case n = 5, and largest number = 3
# lower bond: n - 3 = 2 ,meaning 2 numbers are never shown == extraDupTime >= 2
# higher bond: n, at most duplicate 5 times 
# since we already mentioned this extaDupTime = 2n, so only [2,4] are possible values. 
# (x1-y1) / 2 = 3, (x1-y1)/4 = 1.5 , so we get our resultNumber = 3

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
            
        #go through once, find lowest, highest, sum of all, ^ of all
        lowest = nums[0]
        highest = nums[0]
        sumAll = nums[0]
        DiffAll = nums[0]
        result = -1
        
        for i in range(1, len(nums)):
            sumAll += nums[i]
            DiffAll ^= nums[i]
            
            if nums[i] < lowest:
                lowest = nums[i]
            elif nums[i] > highest:
                highest = nums[i]
        
        if lowest == highest: # only one number in the array
            return lowest
            
        DiffRange = lowest #lowest ^ lowest+1 ^... ^ highest
        SumRange = lowest  #lowest + (lowest+1) + ... + highest
        for num in range(lowest+1, highest+1):
            DiffRange ^= num
            SumRange += num
        
        if DiffRange != DiffAll # extra repeat (2n+1) times, same as repeat 1 time extra for Diff values
            return DiffRange ^ DiffAll

        # extra repeat 2n times
        ExtraRepeatTimes = []
        sumDiff = sumAll - SumRange # (sumDiff = resultNumber * timeOfExtraRepeat) , which is 2n
        
        lowBond = len(nums) - highest + (lowest - 1) # missing numbers in (1,...,n) 
        highBond = len(nums) - 2  # only two numbers
        
        #limit these bonds more
        if sumDiff/lowest < highBond:  # resultNumber has to be in [lowest, .., highest]
            highBond = sumDiff/lowest
        if sumDiff/highest > lowBond:
            lowBond = sumDiff/highest
        
        # any 2n between lowBond and highBond is possible extra repeating times
        for num in range(lowBond, highBond+1):
            if num%2 == 0:
                ExtraRepeatTimes.append(num)
                
        for times in ExtraRepeatTimes:
            if sumDiff % times == 0 and sumDiff/times 
                
        
        
        
