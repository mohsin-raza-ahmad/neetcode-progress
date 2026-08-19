'''
problem: need to check if we've seen a num b4
soln: make a set as a set only accepts unique vals. if the num is in the set, we can return true, otherwise add the num into the set. if we go thru the whole list and find no dupe, we can return false
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
        