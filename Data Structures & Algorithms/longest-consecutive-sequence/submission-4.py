class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ver = set(nums)
        longest = 0
        for num in set_ver:
            length = 0
            if num-1 not in set_ver:
                while num+length in set_ver:
                    length += 1
                longest = max(longest,length)
        return longest