'''
idea: substring alludes to sliding window technique. 
make a set cuz they dont contain dupes. loop thru the string and if the
letter is  in the set add, remove it and increment left pointer, else
add  the letter on the right pointer. return the max window. 
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        r = 0
        maxs = 0
        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxs = max(maxs, r-l+1)
            r+=1
        return maxs
        