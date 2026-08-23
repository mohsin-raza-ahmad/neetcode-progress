'''
Problem: need a way to see 1 part of a string is the same as the other.
idea: have two variables (pointers) that go thru the string. one from the start, one at the end. make the start go forwards and the end go back. check if chars are equal. if yes, continue, if not break, and stop when start pointer > end pointer (not >= cuz obvi itll be the same letter)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 



        

        