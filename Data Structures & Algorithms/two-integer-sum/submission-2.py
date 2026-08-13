class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Thoughts: I need 2 indicies which hold values summing to a target.
        So, i need to keep track of the index AND val of my list. Thus, a hashmap. To get my target, i can find the diff between my target and the current val/index. if the val is in my hashmap on the current iteration, i know i can use that + my current iteration to get my target. thus, i can return the index of the diff in my hashmap and the index of the current iteration.
        '''
        hashmap = {}
        for i, j in enumerate(nums): #to get both index + val
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i