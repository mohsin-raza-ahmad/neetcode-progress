'''
idea: we know the day is in chronological order so go in order not from 
1 end to another. make a window that gives us the most profit. if we prices[r] < prices [l], move l to r
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                curp = prices[r]-prices[l]
                maxp = max(curp,maxp)
            else:
                l=r
            r+=1
        return maxp