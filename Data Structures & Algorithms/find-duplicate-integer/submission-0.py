class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for number in nums:
            if number in seen:
                return number
            seen.add(number)
        return -1