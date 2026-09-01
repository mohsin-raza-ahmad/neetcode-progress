'''
thoughts: substring = sliding window.
if t == "" or t > s, return ""
we'll have 2 maps. 1 map for t that doesnt change. and 1 for s, thatll change based on the window. we'll have a have var that reps what we have in our window and a need var that we need to get. we'll also have a res list that reps the indicies that is our smallest window and a reslen. if our window is smaller than reslen, we update reslen. return the window based on this.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t == "":
            return ""
        smap = {}
        tmap = {}
        for i in range(len(t)):
            tmap[t[i]] = 1 + tmap.get(t[i], 0)
        have = 0
        need = len(tmap)
        res = [-1,-1]
        reslen = float('infinity')
        l = 0
        r = 0 
        while r < len(s):
            smap[s[r]] = 1+smap.get(s[r],0)
            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < reslen:
                    res = [l, r]
                    reslen = r-l+1
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l+=1
            r+=1
        l = res[0]
        r = res[1]
        if reslen != float("infinity"):
            return s[l:r+1]
        else:
            return ""
        