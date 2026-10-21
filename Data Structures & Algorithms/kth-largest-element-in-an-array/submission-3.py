
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        -unsorted arr of ints -> nums
        -return kth largest ele in nums in sorted order
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums) 
        return nums[-k]           
        