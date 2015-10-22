# this is the leetcode expected version, only handle expression starting with number. "-2-4" would consider invalid input and can't be handled properly with this solution
class Solution(object):
    allOps = ['+','-','*']
    
    def opResult(self, num1, num2, op):
        if op == "+":
            return num1 + num2;
        
        if op == "-":
            return num1 - num2;
            
        if op == "*":
            return num1*num2;
    
    # return all results in a list for list ops and list nums
    def getAllResults(self, ops, nums):
        if (ops is None or len(ops) == 0) and len(nums) == 1:
        	return nums
            
        # one op and two numbers
        if len(ops) == 1 and len(nums) == 2:
            return [self.opResult(nums[0],nums[1],ops[0])]
        
        result = []
        # more than one op 
        # nums[0] ops[0] (self.getAllResults(ops[1:], nums[1:])
        #((self.getAllResults(ops[0:1], nums[0:2])) ops[1] (self.getAllResults(ops[2:], nums[2:]))
        #((self.getAllResults(ops[0:2], nums[0:3])) ops[2] (self.getAllResults(ops[3:], nums[3:]))
        #....
        #((self.getAllResults(ops[0:len(ops)-1], nums[0:len(ops)])) ops[len(ops)-1] nums[len(ops)])    
        for i in range(0,len(ops)):
        	num1List = self.getAllResults(ops[0:i], nums[0:i+1])
        	op = ops[i]
        	num2List = self.getAllResults(ops[i+1:], nums[i+1:])
        	for num1 in num1List:
        		for num2 in num2List:
        			result.append(self.opResult(num1, num2, op))
       
        return result
        
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input is None or len(input) == 0:
            return []
            
        ops = []
        nums = []
        result = []
        opsIndex =[]
        for i in range(0,len(input)):
        	if input[i] in self.allOps:
        		opsIndex.append(i)
        		ops.append(input[i])
    	
    	start = 0
    	for i in opsIndex:
    		nums.append(int(input[start:i]))
    		start = i+1
    	
    	#append last number after last op	
    	nums.append(int(input[start:]))
                
        if len(ops) < 1:
            return nums
        
        return self. getAllResults(ops,nums)
                