'''
thoughts: if t is "" or smaller than s, return "". 
make a map for the window and the t string. t string wont change so fill that up first. ull need a res list that reps the indicies of ur window and a reslen which we set to a big ass num so it can change. 
we'll have a have var and a need var. while have == need, we gotta remove the char at the l pointer. update have accordingly.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        window = {}
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        res = [-1,-1]
        reslen= float("infinity")
        have = 0
        need = len(countT)
        l = 0
        r = 0
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have+=1
            while have == need:
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
            r+=1
        l = res[0]
        r = res[1]
        if reslen != float("infinity"):
            return s[l:r+1]
        else:
            return ""

