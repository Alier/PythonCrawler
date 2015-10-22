#Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#Example 1
#Input: "2-1-1".

#((2-1)-1) = 0
#(2-(1-1)) = 2
#Output: [0, 2]


#Example 2
#Input: "2*3-4*5"

#(2*(3-(4*5))) = -34
#((2*3)-(4*5)) = -14
#((2*(3-4))*5) = -10
#(2*((3-4)*5)) = -10
#(((2*3)-4)*5) = 10
#Output: [-34, -14, -10, -10, 10]

class Solution(object):
    allOps = ['+','-','*']
    
    def opResult(self, num1, num2, op):
    	print "op: "+str(num1)+ str(op) +str(num2)
        if op == "+":
            return num1 + num2;
        
        if op == "-":
            return num1 - num2;
            
        if op == "*":
            return num1*num2;
    
    # return all results in a list for list ops and list nums
    def getAllResults(self, ops, nums):
        print "===== this round ====="
        print ops
        print nums
        
        if len(ops) == 0 and len(nums) == 1:
        	#return nums
        	print "return"
        	print nums
        	return nums
            
        # one op and two numbers
        if len(ops) == 1 and len(nums) == 2:
            print "return"
            print [self.opResult(nums[0],nums[1],ops[0])]
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
        	print "num1List and num2List"
        	print num1List
        	print num2List
        	for num1 in num1List:
        		for num2 in num2List:
        			print "num1="+str(num1)+"/num2="+str(num2)
        			result.append(self.opResult(num1, num2, op))
        	print "for i = "+str(i) +"adding result:"
        	print result
        	
        print "return:"
        print result
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
    	
    	print opsIndex
    	start = 0
    	for i in opsIndex:
    		if i == 0:
    			start = i+1
    			continue
    		
    		nums.append(int(input[start:i]))
    		start = i+1
    		
    	nums.append(int(input[start:]))
        print nums
        print ops
                
    	if len(ops) < 1:
    		return nums
    		
        if len(ops) == len(nums) and ops[0] == "-":
        	result1 = self.getAllResults(ops[1:], nums)
        	print "result1:"
        	print result1
        	for re in result1:
        		result.append(-re)
        	
        	nums[0] = -nums[0]
        	result2 = self.getAllResults(ops[1:], nums)
        	print "result2"
        	print result2
        	for re in result2:
        		result.append(re)
        	
    	else:
        	result = self. getAllResults(ops,nums)
        
        return result

st = Solution()
print st.diffWaysToCompute("2-4*3")
#print result