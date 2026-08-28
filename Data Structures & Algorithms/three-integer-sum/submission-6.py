class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                tot = val + nums[l] + nums[r]
                if tot < 0:
                    l+=1
                elif tot > 0:
                    r-=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r:
                        l+=1
        return res