class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {")":"(","]":"[","}":"{"}
        for bracket in s:
            if bracket in closed:
                if stack and stack[-1] == closed[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if not stack:
            return True
        else:
            return False