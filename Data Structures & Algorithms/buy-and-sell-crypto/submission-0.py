class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        minLeft = prices[0]

        for i in range(1,len(prices),1):
            minLeft = min(minLeft,prices[i])
            cur = prices[i] - minLeft
            profit = max(profit,cur)

        return profit


        