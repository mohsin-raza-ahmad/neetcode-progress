'''
thoughts: make a hashmap thatll compare the freqs and chars in both windows (like the valid anagram problem). the first window in s2 will be upto the length of s1. check if full match. if not, continue the window. everytime u add a char in s2, remove the char at the left pointer. 
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1chars = {}
        s2chars = {}
        for i in range(len(s1)):
            if s1[i] in s1chars:
                s1chars[s1[i]] += 1
            else:
                s1chars[s1[i]] = 1
            if s2[i] in s2chars:
                s2chars[s2[i]] += 1
            else:
                s2chars[s2[i]] = 1
        if s1chars == s2chars:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            if s2[r] in s2chars:
                s2chars[s2[r]] +=1
            else:
                s2chars[s2[r]] = 1
            s2chars[s2[l]] -=1
            if s2chars[s2[l]] == 0:
                del s2chars[s2[l]]
            if s1chars == s2chars:
                return True
            l+=1
            r+=1
            
        return False

         


