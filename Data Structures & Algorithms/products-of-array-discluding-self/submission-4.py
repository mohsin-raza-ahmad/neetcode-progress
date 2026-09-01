'''
thoughts: we can make a result list that is 1 in every index. then multiply all left indexes at every index. then do the opposite.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        preval = 1
        for i in range(len(nums)):
            res[i] = preval
            preval *= nums[i]
        postval = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postval
            postval *= nums[i]
        return res
        