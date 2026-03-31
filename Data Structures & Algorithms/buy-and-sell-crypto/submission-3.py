class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        peakProfit = 0
        minPrice = prices[0]
        l, r = 0, 0
        
        for price in prices:
            profit = price - minPrice

            if profit > peakProfit:
                peakProfit = profit

            if price < minPrice:
                minPrice = price
        
        return peakProfit

