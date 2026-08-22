'''
prob: find a way to get the biggest consecutive seq
to do: ik a sequence starts when the start - 1 is not in the list. i can check how long this sequence lasts. return the longest seq. use set cuz i need existence of vals only.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            length = 0
            if (num-1) not in numset:
                while (num+length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest
        