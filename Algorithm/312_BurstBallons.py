class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[0] * nums[1] + max(nums)

        if len(nums) == 3:
            # burst middle one first
            return nums[0] * nums[1] * nums[2] + \
                   nums[0] * nums[2] +\
                   max([nums[0],nums[2]])

        if len(nums) == 4:
            # burst either one of the middle two first
            burstLeftMid = nums[0] * nums[1] * nums[2] +\
                           self.maxCoins([nums[0],nums[2],nums[3]])
            burstRightMid = nums[1] * nums[2] * nums[3] +\
                           self.maxCoins([nums[0],nums[1],nums[3]])
            return max(burstLeftMid, burstRightMid)
        
        result = 0
        # burst dents in the middle (not head, or end), dent meaning its previous and latter are both larger than itself
        while len(nums) > 4:
            i = 0
            up = True
            haveDent = False
            peak = -1
            while i < len(nums) -1:
                if up:
                    if nums[i+1] < nums[i]:
                        up = False
                        peak = i
                else:
                    if nums[i+1] >= nums[i]: # i is dent
                        print "Bursting Dent: nums[%d]: %d" % (i, nums[i])
                        result += nums[i-1] * nums[i] * nums[i+1]
                        print "result = %d" % result
                        del nums[i]
                        haveDent = True
                        up = True
                        i -= 1
                i +=1
            if haveDent:
                print "HAVE dent: nums= %r" % nums

            # all Dents bursted, middle are in increasing/decreasing order
            # 1 & 2: middle increasing, 3 & 4: middle decreasing
            # 1. [2, 3, 4, 5, 6]
            # 2. [3, 4, 5, 6, 2]
            
            # 3. [2, 6, 5, 4, 3]
            # 4. [6, 5, 4, 3, 2]

            # 5. [2, 5, 6, 4, 3]
            if not haveDent:
                print "NO dent: nums= %r, peak = nums[%d] = %d" % (nums, peak, nums[peak])
                # delete from peak towards head and towards tail :[1, peak] and [peak+1, len(nums)]
                if peak <= 1: #case 3 & 4
                    while (len(nums) > 4):
                        burst = nums[peak] * nums[peak+1] *nums[peak+2]
                        result += burst
                        print "Bursting nums[%d]: %d" % (peak+1, nums[peak+1])
                        print "result = %d" % result
                        del nums[peak+1]
                elif peak >= len(nums)-2: # case 1 & 2
                    while (len(nums) > 4):
                        burst = nums[peak-2] * nums[peak-1] *nums[peak]
                        result += burst
                        print "Bursting nums[%d]: %d" % (peak-1, nums[peak-1])
                        print "result = %d" % result
                        del nums[peak-1]
                        peak -= 1
                else:  # case 5, peak > 1 and peak < -2, burst peak first
                    while peak > 1 and peak < len(nums)-2:
                        burst = nums[peak-1] * nums[peak] *nums[peak+1]
                        result += burst
                        print "Bursting nums[%d]: %d" % (peak, nums[peak])
                        print "result = %d" % result
                        del nums[peak]
                        if nums[peak-1] > nums[peak]:
                            peak -= 1
                    
        print "nums = %r" % nums
        result += self.maxCoins(nums)
        return result
