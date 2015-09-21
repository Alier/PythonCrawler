class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        
        #sort the array increasing
        incCitations = sorted(citations)
        
        midIndex = len(incCitations)/2   
        countFromMid = len(incCitations) - midIndex
        
        if incCitations[midIndex] == countFromMid:
            return countFromMid
            
        if incCitations[midIndex] > countFromMid:
            while midIndex >= 0 and incCitations[midIndex] > countFromMid:
                midIndex -= 1
                countFromMid += 1
            if midIndex < 0 or incCitations[midIndex] < countFromMid:
                return countFromMid - 1
            else: #incCitations[midIndex] == countFromMid:
                return countFromMid
                
        else: # incCitations[midIndex] < countFromMid:
            while midIndex <= len(incCitations) - 1 and incCitations[midIndex] < countFromMid:
                midIndex += 1
                countFromMid -= 1
            if midIndex >  len(incCitations) - 1:
                return 0
            else:# incCitations[midIndex] >= countFromMid:
                return countFromMid
                 
       