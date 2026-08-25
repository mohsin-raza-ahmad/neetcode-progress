class Solution:

    def encode(self, strs: List[str]) -> str:
        end_str = ""
        for s in strs:
            end_str += str(len(s)) + "-" + s
        return end_str

    def decode(self, s: str) -> List[str]:
        end_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "-":
                j+=1
            length= int(s[i:j])
            end_list.append(s[j+1:j+1+length])
            i = j+1+length
        return end_list
