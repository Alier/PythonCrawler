class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
            
        profit = 0
        i = 0
        flag = -1 #buy = -1, sell = 1
        
        while i+1 < len(prices):
            if prices[i] < prices[i+1] and flag == -1: #buy signal
                #print "buy at price:" + str(prices[i])
                profit = profit + flag*prices[i]
                flag = 0 - flag
            elif prices[i] > prices[i+1] and flag == 1: # sell signal
                #print "sell at price:" + str(prices[i])
                profit = profit + flag*prices[i]
                flag = 0 - flag
            i = i+1
            
        # over and not sold    
        if flag == 1:
            profit = profit + flag*prices[i]
            
        return profit