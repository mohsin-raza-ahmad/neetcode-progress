'''
thoughts: we know the area may range from 1 side of the array to another. thus, two pointers. we know we should sacrfice width for height becuase width is monotonically increasing.
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        biga = 0
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            biga = max(biga, height*width)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return biga

        