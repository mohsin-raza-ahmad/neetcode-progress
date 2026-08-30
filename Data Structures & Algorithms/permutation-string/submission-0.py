'''
thoughts: dealing w substrings so need a window. 


'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1count = {}
        s2count = {}

        # make frequency maps for s1 and first window of s2
        for i in range(len(s1)):
            if s1[i] in s1count:
                s1count[s1[i]] += 1
            else:
                s1count[s1[i]] = 1

            if s2[i] in s2count:
                s2count[s2[i]] += 1
            else:
                s2count[s2[i]] = 1

        if s1count == s2count:
            return True

        l = 0
        r = len(s1)

        while r < len(s2):

            # add new right character
            if s2[r] in s2count:
                s2count[s2[r]] += 1
            else:
                s2count[s2[r]] = 1

            # remove left character
            s2count[s2[l]] -= 1

            if s2count[s2[l]] == 0:
                del s2count[s2[l]]

            l += 1
            r += 1

            if s1count == s2count:
                return True

        return False

        