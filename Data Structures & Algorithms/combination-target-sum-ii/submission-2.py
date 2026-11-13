class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        def backtrack(index, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining < 0 or index == len(candidates):
                return
            path.append(candidates[index])
            backtrack(index + 1, remaining - candidates[index])
            path.pop()
            while (index + 1 < len(candidates)
                   and candidates[index + 1] == candidates[index]):
                index += 1
            backtrack(index + 1, remaining)
        backtrack(0, target)
        return result