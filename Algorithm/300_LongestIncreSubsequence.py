class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 2
            else:
                return 1
            
        curSeqs =[[nums[0]]]
        for i in range(1, len(nums)):
            flagAppended = False
            flagInserted = False
            curSeqLen = len(curSeqs)
            insertSeqIndex=[]
            print "i="+str(i)
            for j in range(0, curSeqLen):
                print "j="+str(j)
                print curSeqs
                seq = curSeqs[j]
                if nums[i] > seq[-1]:
                    seq.append(nums[i])
                    flagAppended = True
                elif nums[i] > seq[0]: # for example, for [2,5,7], next element is 3, then need to append [2,3] to the list 
            		insertSeqIndex.append(j)
            		
            if not flagAppended: # 
                for ind in insertSeqIndex:
                    seq = curSeqs[ind]
                    newList = []
                    for n in seq:
                        if n < nums[i]:
                            newList.append(n)
                    newList.append(nums[i])
                    curSeqs.append(newList)
                    flagInserted = True
            
            if not flagAppended and not flagInserted: # new lowest point, new starting point
                curSeqs.append([nums[i]])
            
        print "final curSeqs:"
        print curSeqs
        maxLen = 0

        for seq in curSeqs:
            if len(seq) > maxLen:
                maxLen = len(seq)
                
        return maxLen
        
st = Solution()
print st.lengthOfLIS([10,9,2,5,3,4])