'''
Problem: make a string from which i can indicate each item in a given list. With this new string, I need to be able to return the original list I was given
To do: Add a num representing the len of the item in the list and add a delimeter following this number. Then, add on the string to the end of this sequence: resulting string = (len(i)) + delimeter + string. This gives manipulated string.
To turn back into the list, we can use these numbers and delimeters as benchmarks to fill a resulting list with the original items at their indexes.
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        end_string = ""
        for string in strs:
            end_string += str(len(string)) + "-" + string
        return end_string

    def decode(self, s: str) -> List[str]:
        end_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "-":
                j += 1
            length = int(s[i:j])
            end_list.append(s[j+1: j+1+length])
            i = j + 1 + length
        return end_list
