class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # to store the val: index
        for i, j in enumerate(nums): # i = index, j = val
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i


            
                

            
            



        

        