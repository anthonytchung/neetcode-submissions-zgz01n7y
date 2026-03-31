class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        peakProfit = 0
        left, right = prices[0], prices[0]
        for price in prices:
            right = price
            left = min(left, price)
            profit = right - left
            peakProfit = max(peakProfit, profit)
        return peakProfit
        