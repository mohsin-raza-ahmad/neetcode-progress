class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for ind,num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], ind]
            else:
                hash[num] = ind