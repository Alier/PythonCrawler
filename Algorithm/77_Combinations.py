class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = list()
        if k == 0 or n < 1 or n < k:
            return result
        
        pool = list()
        for i in range(1,n+1):
            pool.append(i)
            
        if n == k:
            result.append(pool)
            return result
          
         # remove each element from pool would be all the combs   
        if n == k + 1:
            for i in range(1,n+1):
                curList = list(pool)
                curList.remove(i)
                result.append(curList)
            return result

        if k == 1:
            for i in range(1,n+1):
                result.append([i])
            return result
        
        # f(n=5,k=2) = 5 merge f(4,1) + 4 merge f(3,1) + 3 merge f(2,1) + 2 merge f(1,1)
        for i in range(n,k-1,-1): # i should take values [n,k]
            curNum = i
            curComb = self.combine(i-1,k-1)
            newComb = self.mergeIntIntoLists(curNum,curComb)
            for comb in newComb:
                result.append(comb)
        
        return result
        
    # example f(4,[[1,2],[2,3]]) would get return :[[1,2,4],[2,3,4]]    
    def mergeIntIntoLists(self,num,combs):
        if combs is None or len(combs) < 1:
            return combs
            
        for comb in combs:
            comb.append(num)
        
        return combs
            