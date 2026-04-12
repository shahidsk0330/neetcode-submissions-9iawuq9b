class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for price in range(len(prices)):
            for nextprice in range(price+1,len(prices)):
              
                if(prices[price] < prices[nextprice]):
                    maxprofit = max(maxprofit, prices[nextprice]-prices[price])
        return maxprofit
        