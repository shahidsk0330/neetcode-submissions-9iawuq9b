class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)):
            max_profit = 0
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
            maxP = max(max_profit, maxP)
        return maxP
        