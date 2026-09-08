class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        maps1 = {}
        maps2 = {}
        for i in range(len(s1)):
            maps1[s1[i]] = 1 + maps1.get(s1[i], 0)
            maps2[s2[i]] = 1 + maps2.get(s2[i], 0)
        if maps1 == maps2:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            maps2[s2[r]] = 1 + maps2.get(s2[r], 0)
            maps2[s2[l]] -= 1
            if maps2[s2[l]] == 0:
                del maps2[s2[l]]
            if maps1 == maps2:
                return True
            l+=1
            r+=1
        return False
        
