class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_found = prices[0]
        max_profit = 0

        for price in prices:
            min_found = min(min_found, price)
            max_profit = max(max_profit, price - min_found)

        return max_profit