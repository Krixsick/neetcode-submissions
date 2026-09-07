class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = []
        """ 
        -len(arr) = n
        -can be rotated 1 - n times
            -rotating the array 4 times -> last 4 ele to beg
        """
        minimum = nums[0]
        for i in range(1, len(nums)):
            minimum = min(minimum, nums[i])
        return minimum