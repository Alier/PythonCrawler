class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        if len(num) <= 2:
            return num[0]
            
        numOfDigits = dict()
        for number in num:
            if number in numOfDigits.keys():
                if numOfDigits[number] >= len(num)/2:
                    return number
                else:
                    numOfDigits[number] = numOfDigits[number] + 1
            else:
                numOfDigits[number] = 1