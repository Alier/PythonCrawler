class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        #get each digit in a list, check whether the list is symmetric
        # 1221
        res = 0
        num = x
        digits = list()
        while num > 0:
            print num
            res = num % 10 #1, 2, 2, 1
            num = num / 10 #122, 12, 1, 0
            digits.append(res) #{1,2,2,1}
        
        print digits
        #only one digit
        if len(digits) == 1:
            return True
            
        i = 0
        j = len(digits) - 1
        while (i <= j) :
            if digits[i] != digits[j]:
                return False
            else:
                i = i + 1
                j = j - 1

        return True
 
st = Solution()
print st.isPalindrome(-2147447412)
