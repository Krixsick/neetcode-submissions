class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for index in range(1, len(prices)):
            minimum = min(minimum, prices[index])
            if prices[index] > minimum:
                profit += prices[index] - minimum
                minimum = prices[index]
        return profit
