
'''Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
NUM = 0
COUNT =1

class Solution(object):
    def getLowestCount(self, numCounts):
        lowestCount, lowestIndex = numCounts[0][COUNT], 0
        for i in xrange(1, len(numCounts)):
            if numCounts[i][COUNT] < lowestCount:
                lowestCount, lowestIndex = numCounts[i][COUNT], i
        return (lowestCount, lowestIndex)
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [None] *k

        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        numElement = 0
        for num,count in counts.items():
            if numElement < k: # not full
                result[numElement] = (num, count)
                if numElement == 0:
                    curLowestCount = count
                    curHighestCount = count
                    lowCountIndex = 0
                    highCountIndex = 0
                else:
                    if count > curHighestCount:
                        curHighestCount = count
                        highCountIndex = numElement
                    if count < curLowestCount:
                        curLowestCount = count
                        lowCountIndex = numElement
                numElement += 1                        
            else: # numElement == k , full
                if count > curLowestCount:
                    result[lowCountIndex] = (num, count)
                    curLowestCount, lowCountIndex = self.getLowestCount(result)

        return [elem[NUM] for elem in result]
        
st = Solution()
print st.topKFrequent([1,1,1,1,3,2,3,2,2,2,3,4,5],3)
        
