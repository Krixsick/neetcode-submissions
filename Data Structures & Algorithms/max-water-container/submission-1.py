class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        -return max Area given the arr(heights) where heights[i] is the height
        -we may choose any two bars whose area can hold the most water
            -we can choose similar to stock predictior 
            -we can do o(n^2) time by using a two pointer approach
                -for i in range(len(heights)):
                    r = len(heights)
                    while r > i:
                        r -= 1
                - then we have a max var and see which one gives us the greatest area
        """
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            max_area = max(max_area, (width * height))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
