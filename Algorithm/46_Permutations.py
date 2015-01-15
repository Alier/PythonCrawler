class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if num is None or len(num) == 0:
            return None
        
        result = list()
        if len(num) == 1:
            result.append(num)
            return result
            
        if len(num) == 2:
            result.append([num[0],num[1]])
            result.append([num[1],num[0]])
            return result
            
        return self.getNewPermute(num[0],self.permute(num[1:]))
        
    #insert num into each permute in permuteLists to create new permuteLists
    #example input, num = 3, permuteLists = [[1,2],[2,1]]
    #result should be [[3,1,2],[1,3,2],[1,2,3],[3,2,1],[2,3,1],[2,1,3]]
    def getNewPermute(self,num,permuteLists):
        newPermuteLists = list()
        for i in range(0,len(permuteLists)):
            curPermute = permuteLists[i] #[1,2]
            # three gaps to insert to [i,1,i,2,i]
            for j in range(0,len(curPermute)+1):
                newPermute = list(curPermute)
                newPermute.insert(j,num)
                newPermuteLists.append(newPermute)
            #insert to last position, use append
        
        return newPermuteLists