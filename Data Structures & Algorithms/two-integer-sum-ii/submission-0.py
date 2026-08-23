class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(numbers):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff]+1, ind+1]
            else:
                hashmap[num] = ind
