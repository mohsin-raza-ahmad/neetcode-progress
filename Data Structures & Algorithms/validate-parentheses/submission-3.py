'''
thoughts: we can use a stack because we need to compare the top of the list (most recent item) to the item we need to input.
make a stack, and a map that maps closing brackets to open. go thru the string and make sure all elements are being properly added/popped from the stack.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in close_open: # element a closing bracket
                if stack and stack[-1] == close_open[char]: # first val cant be closing
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False




