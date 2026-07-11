class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            reminder = target - nums[index]
            if reminder not in seen:
                seen[nums[index]] = index
            else:
                return [seen[reminder], index]
