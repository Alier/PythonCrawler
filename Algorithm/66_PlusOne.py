class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    # example, [1,0,0,0,0] represents 10000, adding one is easy, [1,0,0,0,1]
    # if original is [9,9,9] then adding one would be : [1,0,0,0]
    
    def plusOne(self, digits):
        if digits is None or len(digits) == 0 :
            return digits
        
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            i = i - 1
        
        if i == -1 : # all digits are 9. add 1 to the first
            digits.insert(0,1)
        else:
            digits[i] = digits[i] + 1
        
        return digits