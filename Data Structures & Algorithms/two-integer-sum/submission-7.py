'''
problem: return indicies which values reside to sum upto a target val.
to do: for every val in nums, check if the difference of the target and the current value is in a hashmap which maps values to their index. if its in it, return the current index and the index in the hashmap. if not, put in the value and index into the hashmap.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i
        