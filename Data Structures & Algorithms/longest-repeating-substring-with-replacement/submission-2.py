'''
idea: get longest susbtring with non-distinct chars and put in an array. return len of array + k
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        l = 0
        r = 0
        longest = 0
        maxf = 0
        while r < len(s):
            if s[r] in char_count:
                char_count[s[r]] +=1
            else:
                char_count[s[r]] = 1
            maxf = max(maxf, char_count[s[r]])
            while (r-l+1) - maxf > k:
                char_count[s[l]] -=1
                l+=1
            longest = max(longest, r-l+1)
            r+=1
        return longest


        