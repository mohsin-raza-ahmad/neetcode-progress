'''
thoughts: a set doesnt accept dupes. thus, loop thru list and add elements not in set. if alr in, return True
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for num in nums:
            if num in numset:
                return True
            else:
                numset.add(num)

        return False
        