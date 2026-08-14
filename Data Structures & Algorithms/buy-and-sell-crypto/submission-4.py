class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        s = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                s = max(s, profit)
            else:
                l = r
            r += 1
        return s