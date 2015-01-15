class Solution:
    known = {(2,2):2}
    # @return an integer
    def uniquePaths(self, m, n):
        
        if m == 0 or n == 0 :
            return 0
            
        if m == 1 or n == 1:
            return 1
       
        if (m,n) in self.known:
            return self.known[(m,n)]
            
        self.known[(m,n)] = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        return self.known[(m,n)]
            