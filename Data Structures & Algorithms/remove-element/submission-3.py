class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for index in range(len(nums)):
            if nums[index] == val:
                continue
            nums[l] = nums[index]
            l += 1
        return l