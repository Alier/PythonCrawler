class Solution(object):
    # saving already calculated index i, ending with index j elements sum cloest to target, value is cloestSum
    # saving as (i,j) : cloestSum
    closestSum = {}
	
	 #function to find 2 numbers in a sorted array that sums closet to target. Return the closet sum
    def twoSumClosest(self, nums, target):
        print "=======nums and target========"
        print nums
        print target
    	smallestSum = nums[0] + nums[1]
    	largestSum = nums[-1] + nums[-2]
    	
    	# smallest > target or largest < target
    	if smallestSum >= target:
			return smallestSum
		
        if largestSum <= target:
			return largestSum
		
        i = 0 # i point to smaller of the two numbers, j point to bigger of the two
        j = len(nums) - 1
        
        while i < j and nums[i] + nums[j] > target:             
            j -= 1
        
        while i< j and nums[i] + nums[j] < target:
            i += 1    
       
        print "i="+str(i)+"j="+str(j)
        curValue = nums[i] + nums[j]
        if curValue == target:
            return curValue
            
        if i > 0:
            lowValue = nums[i-1] + nums[j]
            if abs(lowValue - target) < abs(curValue - target):
                curValue = lowValue
            
            if j < len(nums)-1:
                highValue = nums[i] + nums[j+1]
                if abs(highValue - target) < abs(curValue - target):
                    curValue = highValue
        else:
            if j < len(nums)-1:
                highValue = nums[i] + nums[j+1]
                if abs(highValue - target) < abs(curValue - target):
                    curValue = highValue   
        
        return curValue
    	
    def quickSort(self,nums):
        if len(nums) <= 1:
            return nums
    
        if len(nums) == 2:
            if nums[0] <= nums[1]:
                return nums
            else:
                return [nums[1],nums[0]]
                
        sample = nums[0]
        left = []
        right = []
        for i in range(1, len(nums)):
            if nums[i] <= sample:
                left.append(nums[i])
            else:
                right.append(nums[i])
        
        sortedLeft = self.quickSort(left)
        sortedRight = self.quickSort(right)
        return sortedLeft+[sample]+sortedRight
        
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            return sum(nums)
        
        #sort the array first   
        sortedNums = self.quickSort(nums)
    
    	self.calculated = {}
    	#first three number sum is the closest sum for this three number set	
    	closetSum = sum(sortedNums[0:3])
        self.closestSum[(0,3)] = closetSum
		
		#starting from 4th num, calculate the max sum of 3 numbers out of the current set including nums[0:curIndex+1]
        for i in range(3,len(sortedNums)):
            print self.closestSum
            curNum = sortedNums[i]
            selectSum = curNum + self.twoSumClosest(sortedNums[0:i], target - curNum)
            nonSelectSum = self.closestSum[(0,i)]
            if abs(selectSum - target) < abs(nonSelectSum - target):
                self.closestSum[(0,i+1)] = selectSum
            else:
                self.closestSum[(0,i+1)] = nonSelectSum
			 	 
        return self.closestSum[(0,len(sortedNums))]
	    
st = Solution()
print st.threeSumClosest([1,2,4,8,16,32,64,128],82)