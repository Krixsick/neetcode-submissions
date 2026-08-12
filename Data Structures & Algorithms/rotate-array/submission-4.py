class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reminder = k % len(nums)
        full_len = k // len(nums)
        if full_len > 1:
            for i in range(full_len):
                for j in range(len(nums)):
                    nums.insert(0, nums.pop())

        for k in range(reminder):
            nums.insert(0, nums.pop())

        return nums        