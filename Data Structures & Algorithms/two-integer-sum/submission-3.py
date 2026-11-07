class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftover_nums = {}

        for num in range(len(nums)):
            tmp = target - nums[num]
            if tmp in leftover_nums:
                return [leftover_nums[tmp], num]
            leftover_nums[nums[num]] = num
        return -1