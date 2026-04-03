class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOPen ={"}":"{", ")":"(","]":"["}

        for c in s:
            if c in closeToOPen:
                if stack and stack[-1] == closeToOPen[c]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False