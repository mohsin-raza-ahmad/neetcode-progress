class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        l = 0
        r = 0
        maxf = 0
        longest = 0
        while r < len(s):
            if s[r] in hash:
                hash[s[r]] += 1
            else:
                hash[s[r]] = 1
            maxf = max(maxf, hash[s[r]])
            while (r-l+1) - (maxf) > k:
                hash[s[l]] -= 1
                l+=1
            longest = max(longest, r-l+1)
            r+=1
        return longest

