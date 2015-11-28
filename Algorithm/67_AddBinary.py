class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a is None or len(a) == 0:
            return b
        
        if b is None or len(b) == 0:
            return a
    
        digitCount = max(len(a),len(b))
        result = ""
        toCarry = '0' 
        for i in range(0, digitCount):
            curdigitA = '0'
            curdigitB = '0'
            if len(a)-1-i >= 0:
                curdigitA = a[len(a)-1-i]
            if len(b)-1-i >= 0:
                curdigitB = b[len(b)-1-i]
            
            digitResult = int(curdigitA)+int(curdigitB)+int(toCarry)
            if digitResult >= 2:
                curDigit = str(digitResult-2)
                toCarry = '1'
            else: # digitResult <= 1
                curDigit = str(digitResult)
                toCarry = '0'
            
            result = curDigit+result
        
        if toCarry == '1':
            result = '1'+result
            
        return result