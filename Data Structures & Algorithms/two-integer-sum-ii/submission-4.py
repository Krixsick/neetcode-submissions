class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ 
        -arr of int numbers sorted non-desc order 
            -can use binary search to help us look
        -return two nums that add up to target
            index1 and index2 cannot be the same
        """
        l, r = 0, len(numbers) - 1
        while l < r: 
            val = numbers[l] + numbers[r]
            if val == target:
                return [l + 1, r + 1]
            elif val < target:
                l += 1
            else:
                r -= 1
        return []

