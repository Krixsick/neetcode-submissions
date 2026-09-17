class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = int("".join(map(str, digits))) + 1
        output = [int(digit) for digit in str(value)]
        return output