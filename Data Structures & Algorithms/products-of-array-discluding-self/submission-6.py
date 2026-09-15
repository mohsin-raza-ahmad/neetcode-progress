class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        preval = 1
        for num in range(len(nums)):
            res[num] = preval
            preval *= nums[num]
        postval = 1
        for num in range(len(nums)-1,-1,-1):
            res[num] *= postval
            postval *= nums[num]
        return res