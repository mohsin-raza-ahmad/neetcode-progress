class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height)-1
        leftM = height[l]
        rightM = height[r]
        total = 0
        while l < r:
            if leftM<rightM:
                l+=1
                leftM = max(leftM, height[l])
                total += leftM - height[l]
            else:
                r-=1
                rightM = max(rightM, height[r])
                total += rightM - height[r]
        return total