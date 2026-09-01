'''
thoughts: a palindrome checks if the string is the same from both respective sides. so, we can use a double pointer technique. until l < r, go thru the string and check if each side is ==.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
            