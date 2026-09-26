class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        values = {}
        for number in nums:
            if number not in values:
                values[number] = values.get(number, 0) + 1
            else:
                values[number] += 1
        for key, value in values.items():
            if value == 1:
                return key