class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            while s[r] in sset:
                sset.remove(s[l])
                l+=1
            sset.add(s[r])
            longest = max(longest, r-l+1)
            r+=1
        return longest