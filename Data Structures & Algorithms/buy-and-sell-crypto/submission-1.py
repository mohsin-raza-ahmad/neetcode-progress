class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = 0
        r = 1
        max_prof = 0
        while r < len(prices):
            cur_prof = prices[r] - prices[l]
            max_prof = max(max_prof, cur_prof)
            if prices[r] > prices[l]:
                r+= 1
            else:
                l=r
                r+=1
        return max_prof




            
