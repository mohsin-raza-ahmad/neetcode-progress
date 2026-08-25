'''
idea: make a biggest area var, and a biggest height var. set the biggest area to the area of indicie 1 to the end. decrement the 
'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggesta = 0
        l = 0
        r = len(heights)-1
        while l < r:
            height = min(heights[l],heights[r])
            width = r - l
            area = height * width
            if area > biggesta:
                biggesta = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return biggesta
            