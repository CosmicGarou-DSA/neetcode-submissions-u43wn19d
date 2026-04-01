class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=float('inf')
        max_p=0
        profit=0
        for i in range(len(prices)):
            min_p=min(min_p,prices[i])
            profit=prices[i]-min_p
            max_p=max(max_p,profit)
        return max_p