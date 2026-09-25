from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()
        result = []
        for r in range(len(nums)):
            left = r - k + 1
            while candidates and candidates[0] < left:
                candidates.popleft()
            while candidates and nums[candidates[-1]] <= nums[r]:
                candidates.pop()
            candidates.append(r)
            if r >= k - 1:
                result.append(nums[candidates[0]])
        return result