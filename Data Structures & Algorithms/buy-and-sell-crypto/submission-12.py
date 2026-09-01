'''
thoughts: as day matters and its in chronological order, we need to use a sliding window. track the profit at a window, keep going until u find a new day to buy.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                curp = prices[r] - prices[l]
                maxp = max(maxp,curp)
            else:
                l=r
            r+=1
        return maxp
        