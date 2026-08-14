class Solution:

    def encode(self, strs: List[str]) -> str:
        end_res =''
        for i in strs:
            end_res += str(len(i)) + "$" + i
        return end_res
    def decode(self, s: str) -> List[str]: # s = '3$Ate2$Hi'
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
