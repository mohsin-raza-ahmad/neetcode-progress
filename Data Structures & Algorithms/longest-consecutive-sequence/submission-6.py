'''
thoughts: we only need to focus on the set because we dont care abt dupes. 
we can keep track of the lonegst sequence, and keep track of the length of the current seq. we know if we're at a start of a (possible) seq if num-1 not in set. return longest.

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            length = 0
            if num-1 not in nums_set:
                while num+length in nums_set:
                    length += 1
            longest = max(longest, length)
        return longest

        