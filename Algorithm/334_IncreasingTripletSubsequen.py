class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) < 3:
            return False

        triplet = []
        Decrease = True

        for i in xrange(len(nums)-1):
            if len(triplet) != 0 and nums[i] > triplet[-1]:
                triplet.append(nums[i])
                if len(triplet) >= 3:
                    print triplet
                    return True
                
            elif Decrease and nums[i+1] > nums[i]: # bottom points
                Decrease = False
                if len(triplet) == 0:
                    triplet.append(nums[i])
                    triplet.append(nums[i+1])
                else: # may need merge
                    if nums[i] > triplet[0]:
                        triplet[1] = nums[i]
                        triplet.append(nums[i+1])
                        print triplet
                        return True
                    elif nums[i+1] < triplet[1]:
                        triplet[0] = nums[i]
                        triplet[1] = nums[i+1]                     
            elif not Decrease and nums[i+1] <= nums[i]: # top points
                Decrease = True

        #handle last one
        if i == maxIdx - 1:
            if len(triplet) != 0 and nums[i+1] > triplet[-1]:
                triplet.append(nums[i+1])
                if len(triplet) >= 3:
                    print triplet
                    return True
                
        return False
