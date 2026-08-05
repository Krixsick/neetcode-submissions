class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        -return smallest positive int
        -is 0 considered a positive int? no from ex 2
        -how can we determine smallest?
        -brute force
            -since it's 1 <= num.length <= 100k
                -you do i in range(100001)
                -see if that number is in it or not 
        """
        for i in range(1, 100001):
            if i not in nums:
                return i