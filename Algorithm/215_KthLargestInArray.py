class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2) :
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot                
                
st = Solution()
print st.findKthLargest([7,6,5,4,3,2,1], 5)