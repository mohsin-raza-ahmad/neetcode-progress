class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        Idea: given a list, make a string where each item of the list is now identifiable
        '''
        end_string = ""
        for string in strs:
            end_string += str(len(string)) + "-" + string #length of item+delimeter+string
        return end_string

    def decode(self, s: str) -> List[str]:
        '''
        Idea: given the manipulated string, make a list where each item is correct og item
        '''
        end_list = []
        pre_ind = 0
        while pre_ind < len(s):
            aft_ind = pre_ind
            while s[aft_ind] != "-":
                aft_ind += 1
            length = int(s[pre_ind:aft_ind])
            end_list.append(s[aft_ind + 1:aft_ind + 1 + length])
            pre_ind = aft_ind + 1 + length

        return end_list