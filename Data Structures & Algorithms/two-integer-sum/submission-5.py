class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val: index
        for index, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[val] = index
        
        