'''
thoughts: substring = sliding window. permutation is basicaly an anagram. make 2 maps, 1 for s2 and 1 for s1. if the 2 windows are ever equal, return true. every time u add a char, delete 1 from the start of the window.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = {}
        s2count = {}
        for char in range(len(s1)):
            s1count[s1[char]] = 1 + s1count.get(s1[char], 0)
            s2count[s2[char]] = 1 + s2count.get(s2[char], 0)
        if s1count == s2count:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            s2count[s2[r]] = 1 + s2count.get(s2[r], 0)
            s2count[s2[l]] -= 1
            if s2count[s2[l]] == 0:
                del s2count[s2[l]]
            if s1count == s2count:
                return True
            l+=1
            r+=1
        return False
