'''
thougghts: substring = sliding window. we dealing w dupes so sets. go thru the string and add chars until we see a dupe. remove the start of the window while the char is in the set. keep track of the longest window.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        s_set = set()
        while r < len(s):
            while s[r] in s_set:
                s_set.remove(s[l])
                l+=1
            s_set.add(s[r])
            longest = max(longest, r-l+1)
            r+=1
        return longest
        