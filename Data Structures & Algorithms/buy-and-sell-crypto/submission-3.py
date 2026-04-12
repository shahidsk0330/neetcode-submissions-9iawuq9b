class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        window = set()
        window.add(prices[0])
        for i in range(1,len(prices)):
            buying = min(window)
            maxP = max(maxP, prices[i]-buying)
            window.add(prices[i])
        return maxP
            
        