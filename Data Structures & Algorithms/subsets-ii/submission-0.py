class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        result = []
        path = []
        def backtrack(index):
            if index == len(nums):
                if tuple(path) in visited:
                    return
                visited.add(tuple(path.copy()))
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()
            backtrack(index + 1)
        backtrack(0)
        return result