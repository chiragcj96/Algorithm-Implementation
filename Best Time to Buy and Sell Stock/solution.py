class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        maximum = 0
        minimum = 10**4
        maxprofit = 0
        for i in range(len(prices)):
            if maximum<prices[i]:
                maximum=prices[i]
            if minimum>prices[i]:
                minimum=prices[i]
                maximum=0
            print(maximum, minimum)
            maxprofit = max(maxprofit, maximum-minimum)
        if maxprofit>0:
            return maxprofit
        else:
            return 0
    

        