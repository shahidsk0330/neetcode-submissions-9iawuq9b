class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxprofit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxprofit = max(maxprofit, price - minPrice)
        return maxprofit
        