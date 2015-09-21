#Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#The same repeated number may be chosen from C unlimited number of times.

#Note:
#All numbers (including target) will be positive integers.
#Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#The solution set must not contain duplicate combinations.
#For example, given candidate set 2,3,6,7 and target 7, 
#A solution set is: 
#[7] 
#[2, 2, 3] 
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0:
            return []
            
        candidates = sorted(candidates)
        return self.combinationSumSorted(candidates, target)
        
    def combinationSumSorted(self, candidates, target):
        result = []
        
        if candidates is None or len(candidates) == 0:
            return result
        
        if candidates[0] > target:
            return result
        
        for i in range(0,len(candidates)) :
            curElem = candidates[i]
            newCandidates = candidates[i:]
            newTarget = target - curElem
            if newTarget < 0:
                return result
            elif newTarget == 0:
                result.append([curElem])
            else:
                subSets = self.combinationSumSorted(newCandidates, newTarget)
                for s in subSets:
                    if len(s) > 0: # s is not []
                        s.insert(0,curElem)
                        result.append(s)
        
        return result