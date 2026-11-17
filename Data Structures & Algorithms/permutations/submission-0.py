class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return 
            for number in nums:
                if number in path:
                    continue
                path.append(number)
                backtrack()
                path.pop()
        backtrack()
        return result
                
