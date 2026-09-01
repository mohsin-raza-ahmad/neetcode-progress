'''
thoughts: we're given a sorted list, so think of two pointers.
we can use the 2 pointers to get the sum, if total < target, increment, else decrement.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot < target:
                l+=1
            elif tot > target:
                r-=1
            else:
                return [l+1,r+1]
        