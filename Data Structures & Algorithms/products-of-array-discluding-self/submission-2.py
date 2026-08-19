'''
To get the product of every value except ur own index, i need to first get the product of all values left of the index im at, then store that in a resulting list. then, perform a loop a loop which multiplies all values to the right of the index im at in nums with the resulting lists' indexes.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) # initialize all vals to 1 b/c 1*anynum = anynum
        pre_val = 1
        for i in range(len(nums)):
            result[i] = pre_val
            pre_val *= nums[i]
        post_val = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= post_val
            post_val *= nums[i]
        return result