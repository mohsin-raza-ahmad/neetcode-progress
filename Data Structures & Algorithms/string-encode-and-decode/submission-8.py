'''
thoughts: to encode, we can use a int repping the len of the element, a delimeter, and the element itsels. then to decode, we can use these benchmarks to append to our list.
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        end_str = ""
        for string in strs:
            end_str += str(len(string)) + "-" + string
        return end_str
    def decode(self, s: str) -> List[str]:
        end_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "-":
                j+=1
            length = int(s[i:j])
            end_list.append(s[j+1:j+1+length])
            i = j+1+length
        return end_list

