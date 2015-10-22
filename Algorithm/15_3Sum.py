#given a list of integers, find out all three integer combinations that sums up to target
#e.g , for list [-1,1,2,3,4,0,1] and target 2 , return[[-1,1,2],[-1,2,0]]
class Solution(object):
	# return list of two num combinations that sums to target
	calculated = {}
	def twoSum(self, nums, target):		
		if len(nums) < 2:
			return []
		
		if len(nums) == 2:
			if sum(nums) == target:
				return [nums]
			else:
				return []
		
		if nums[0] + nums[1] > target or nums[-1] + nums[-2] < target:
			return []
		
		result = []
		
		for i in range(0,len(nums)):
			if (target - nums[i]) in nums[i+1:]:
				result.append([nums[i],target-nums[i]])
        
		return result
    
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
        
	def threeSumTarget(self, nums, endIndex, target):
		if endIndex in self.calculated:
			return self.calculated[endIndex]
			
		smallest = sum(nums[:3])
		if smallest == target:
			return [nums[:3]]
		elif smallest > target:
			return []
			
		largest = sum(nums[endIndex-2:])
		if largest == target:
			return [nums[endIndex-2:]]
		elif largest < target:
			return []
		
		# smallest < target < largest
		# threeSum for first three elements is None. 
		self.calculated[2] = [] 
		
		for i in range(3, endIndex+1):
			result = []
			selected = self.twoSum(nums[:i], target-nums[i])
			if len(selected):
				for item in selected:
					item.append(nums[i])
					if item not in result:
						result.append(item)
			nonSelected = self.threeSumTarget(nums, i-1, target)
			if len(nonSelected):
				for item in nonSelected:
					if item not in result:
						result.append(item)
			self.calculated[i] = result
			print "calculated for i= "+str(i) +":"
			print self.calculated[i]
			
		return self.calculated[endIndex]
	
	def threeSum(self,nums):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		if len(nums) < 3:
			return None
        
		if len(nums) == 3:
			if sum(nums) == 0:
				return [nums]
			else:
				return None
        
    	#sort the array first   
		sortedNums = self.quickSort(nums)
		print sortedNums
		return self.threeSumTarget(sortedNums, len(sortedNums)-1, 0)

st = Solution()
print st.threeSum([-1,0,1,2,-1,-4])
#print st.threeSum([1,2,4,8,16,32,64,128],82)	 
#print st.threeSum([-1,0,1,2,-1,-4],0)   	