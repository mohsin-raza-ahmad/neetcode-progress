class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # initalize result list to 1s
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # this allows every index in res to get the left product of every index in nums
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

      
        