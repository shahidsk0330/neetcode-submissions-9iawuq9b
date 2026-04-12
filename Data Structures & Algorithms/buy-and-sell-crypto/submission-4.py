class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuyingDate = prices[0]
        for i in range(1,len(prices)):
            maxP = max(maxP, prices[i]-minBuyingDate)
            minBuyingDate = min(prices[i],minBuyingDate)
        return maxP
            
        