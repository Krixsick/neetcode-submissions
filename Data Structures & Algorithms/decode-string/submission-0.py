class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        amount = 0
        curr_str = ""
        for character in s:
            if character.isdigit():
                amount = amount * 10 + int(character)
            elif character == "[":
                stack.append((curr_str, amount))
                amount = 0
                curr_str = ""
            elif character == "]":
                prev_str, prev_amount = stack.pop()
                curr_str = prev_str + (prev_amount * curr_str)
            else:
                curr_str += character
        return curr_str