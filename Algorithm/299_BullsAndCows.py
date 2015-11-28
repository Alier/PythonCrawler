class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if (secret is None and guess is None) or (len(secret) == 0 and len(guess) == 0):
            return "0A0B"
        
        numA = 0
        numB = 0
        restSecret = ""
        restGuess = ""
    	secretDict = {} # record how many times each number stays
        for i in range(0, len(secret)):
        	if secret[i] == guess[i]:
        		numA += 1
        	else:	
        		restSecret += secret[i]
        		restGuess += guess[i]
        		
        		if secret[i] in secretDict:
        			secretDict[secret[i]] += 1
        		else:
        			secretDict[secret[i]] = 1
        
        print secretDict
        
        for i in range(0, len(restGuess)):
            print "restGuess[i] ="+str(restGuess[i])
            print "i="+str(i)
            print secretDict
            if restGuess[i] in secretDict:
                numB += 1
                secretDict[restGuess[i]] -= 1
            	if secretDict[restGuess[i]] <= 0:
            		secretDict.pop(restGuess[i])
				        
        return str(numA)+"A"+str(numB)+"B"

st = Solution()
print st.getHint("1122","1222")