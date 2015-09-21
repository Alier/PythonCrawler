#Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#Ensure that numbers within the set are sorted in ascending order.

#Example 1:
#Input: k = 3, n = 7
#Output:[[1,2,4]]

#Example 2:
#Input: k = 3, n = 9
#Output:[[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    allCandidates = [1,2,3,4,5,6,7,8,9]
    
    def combinationSum3Recur(self, k, n, candidates):
        result = []
        
        if candidates is None or len(candidates) == 0 or n < 1 or k < 1:
            return result
            
        if k == 1:
            if n in candidates :
                result.append([n])
            return result
            
        for i in range(0,len(candidates)) :
            if candidates[i] >= n:
                return result
            else:
                subSets = self.combinationSum3Recur(k-1,n-candidates[i],candidates[i+1:])
                for s in subSets:
                    if len(s) > 0:
                        s.insert(0,candidates[i])
                        result.append(s)
        
        return result
                    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.combinationSum3Recur(k,n,self.allCandidates)
            
        
            
            