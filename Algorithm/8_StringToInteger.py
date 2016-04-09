import string
import itertools
import sys

# to bypass test 
MAX_POS = 2147483647 
MIN_NEG = -2147483648

class Solution(object):
    def myAtoi(self, str):
        '''
        Implement atoi to convert a string to an integer.
        '''
        """
        :type str: str
        :rtype: int
        """
        if str is None or str == '':
            return 0

        # strip off ' ' in front and end of the string
        str = str.strip()
        symbol = ''
        result = 0
        
        # check first position to see if there is '+-'
        if str[0] in '+-':
            symbol = str[0]
            str = str[1:]
        
        if len(str) == 0:
            return 0
         
         # 0x[digits+'abcdef'] case
        if str[0:2] == '0x' and all([ch in string.hexdigits for ch in str[2:]]):
            result = int(symbol+str[2:], 16)
            if result > 0 :
                return min(MAX_POS, result)
            else:
                return max(MIN_POS, result)
                
        # [digits]e[digits] case
#        if 'e' in str:
#            ind = str.index('e')
#            if ind!= 0 and ind != len(str)-1:
#                if all([ch in string.digits for ch in str[:ind]] or str[ind+1:]):
#                    return float(symbol+str)
                    
        # digits + letters + invalid syms
        # stop counting at the first invalid sym or letter
        firstInvalidl = list(itertools.islice([str.index(ch) for ch in str if ch not in string.digits], 1))
        
        if len(firstInvalidl) == 0:
            # all digits
            result = int(symbol+str)
        else:
            # stop at first letter, if first element in the string is not letter
            if firstInvalidl[0] > 0 :
                result = int(symbol+str[0:firstInvalidl[0]])
                
        if result > 0 :
            return min(MAX_POS, result)
        else:
            return max(MIN_NEG, result)
        
        return 0
        
if __name__ == '__main__':
    args = sys.argv
    st = Solution()
    print st.myAtoi(args[1])
