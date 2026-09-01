'''
thoughts: make a map that contains val: ind. if the diff of the curr val is in the map, we know to return the index in the map and the curr index.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # val:ind
        for ind,val in enumerate(nums):
            diff = target - val
            if diff in map:
                return [map[diff], ind]
            else:
                map[val] = ind
                
        