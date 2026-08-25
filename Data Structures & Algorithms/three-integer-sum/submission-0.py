'''
idea: sort the array to get a situation like two sum 2. then loop thru the indicies and values of the list. if the index is > 0, and we've seen a value b4, continue. else make a left and right pointer going thru the list and increment/decrement accordingly. 

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = val + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    r-=1
                    while nums[l] == nums [l-1] and l < r:
                        l += 1
        return result
            

                
        