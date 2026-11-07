class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"}": "{", "]":"[", ")" : "("}
        stack = []
        for element in s:
            if element not in parenthesis:
                stack.append(element)
            else:
                if stack and parenthesis[element] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack

