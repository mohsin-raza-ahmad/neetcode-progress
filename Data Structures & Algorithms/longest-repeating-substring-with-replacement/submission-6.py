'''
thoughts: substring = sliding window. map to keep track of char and their freq. keep track of the max char in the window. the window - maxchar will tell us to close the window or not. keep track of longest window.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        l=0
        r=0
        maxf=0
        longest = 0
        while r < len(s):
            map[s[r]] = 1 + map.get(s[r], 0)
            maxf = max(maxf, map[s[r]])
            while r-l+1 - maxf > k:
                map[s[l]] -= 1
                l+=1
            longest = max(longest, r-l+1)
            r+=1
        return longest
        