class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(index, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if index == len(nums) or remaining < 0:
                return
            path.append(nums[index])
            backtrack(index, remaining - nums[index])
            path.pop()
            backtrack(index + 1, remaining)
        backtrack(0,target)
        return result