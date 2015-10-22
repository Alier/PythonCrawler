class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        
        #check if there is overlap
        #upper right corner of rectangle A separate from lower left corner of rectangle B
        #lower left corner of A separate from upper right corner of B
        if C < E or D < F or G <A or H < B: 
        	return area1 + area2
        
        if C < G: # right bond, choose lefter right
            overlapC = C
        else:
            overlapC = G
        
        if A < E: # left bond, choose righter left
            overlapA = E
        else:
            overlapA = A
            
        if D < H: # high bond, choose lower high
            overlapD = D
        else:
            overlapD = H
        
        if B < F: # low bond, choose higher low
            overlapB = F
        else:
            overlapB = B
            
        print "("+str(overlapA)+ ","+str(overlapB)+"),("+str(overlapC)+","+str(overlapD)+")"
        areaOverLap = (overlapC-overlapA) * (overlapD - overlapB)
       
        return area1+area2-areaOverLap

st = Solution()
print st.computeArea(-2,-2,2,2,3,3,4,4)