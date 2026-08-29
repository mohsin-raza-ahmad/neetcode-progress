class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            while s[r] in s_set:
                s_set.remove(s[l])
                l+=1
            s_set.add(s[r])
            longest = max(longest, r-l+1)
            r+=1
        return longest

