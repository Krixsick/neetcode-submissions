import heapq
class KthLargest:
    """
        -to find kth largest integer in a stream of vals, we just do
        stream[-kth largest int]
    """
    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
