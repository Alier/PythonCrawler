class Solution:
    maxIndex = 0
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) <= 1:
            return 0
          
        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        
        #save indexs for potential buying and selling in following lists
        buyPoints = list()
        sellPoints = list()
        profit = 0
        
        if prices[0] <= prices[1]:
            buyPoints.append(0)
            
        for i in range(1,len(prices)-1):
            if prices[i-1] < prices[i] and prices[i] >= prices[i+1]:
                sellPoints.append(i)
            elif prices[i-1] > prices[i] and prices[i] <= prices[i+1]:
                buyPoints.append(i)
    
        # i == len(prices)-2
        if prices[i+1] > prices[i]:
            sellPoints.append(i+1)
            
        for buyIndex in buyPoints:
            for sellIndex in sellPoints:
                if sellIndex > buyIndex:
                    curProfit = prices[sellIndex] - prices[buyIndex]
                    if curProfit > profit:
                        profit = curProfit
        
        return profit