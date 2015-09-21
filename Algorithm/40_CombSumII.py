class Solution(object):
    def combinationSum2Sorted(self, candidates, target):
        result = []
        
        if candidates is None or len(candidates)  == 0:
        	return result
        
        for i in range(0, len(candidates)):
            if candidates[i] > target:
        	    return result
        	
            if candidates[i] == target:
        	    result.append([target])
        	    return result
        	    
        	# candidates[i] < target
            subSets = self.combinationSum2Sorted(candidates[i+1:], target-candidates[i])
            if len(subSets) > 0:
                for s in subSets:
                	s.insert(0,candidates[i])
                	result.append(s)
        
        return result
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0:
            return []
        
        all = self.combinationSum2Sorted(sorted(candidates),target)
        
        if len(all) <= 1:
        	return all
        else:
        	ret = []
        	for s in all:
        		if s not in ret:
        			ret.append(s)
        	return ret
        
        
st = Solution()
print st.combinationSum2([2,2,2,2],4)
