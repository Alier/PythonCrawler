class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
            
        result = 0
        residue = 0
        while ( num >= 10 ):
            result = num/10
            residue = residue + (num - result*10)
            num = result
            if residue >= 10 :
                resultResidue = residue/10 
                residueResidue = residue - resultResidue * 10
                residue = resultResidue + residueResidue
                
        total = num + residue
        if total >= 10:
            resultTotal = total/10
            residueTotal = total - resultTotal *10
            total = resultTotal + residueTotal
        
        return total

#print Solution().addDigits(1579)