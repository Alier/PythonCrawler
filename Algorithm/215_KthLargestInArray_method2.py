class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            if nums[0] >= nums[1]:
                return nums[k-1]
            else:
                return nums[2-k]
        
        if k <= len(nums)/2 : # less than half would be in the pool for 1st- kth largest
            pool = [nums[i] for i in range(0,k)] # put first k elements into pool
            pool = sorted(pool)
            for i in range(k, len(nums)): # examine each elem, insert into pool if needed
                if nums[i] > pool[0]:
                    pool.append(nums[i])
                    pool = sorted(pool)
                    print pool
                    del pool[0]
            return pool[0]
        else: # 1-kth largest contains more than half, looks for (n-k)th smallest instead
            k = len(nums) - k+1
            pool = [nums[i] for i in range(0,k)]
            pool = sorted(pool)
            for i in range(k, len(nums)):
                if nums[i] < pool[-1]:
                    pool.append(nums[i])
                    pool = sorted(pool)
                    del pool[-1]
            return pool[-1]
                
st = Solution()
print st.findKthLargest([-1,2,0],1)