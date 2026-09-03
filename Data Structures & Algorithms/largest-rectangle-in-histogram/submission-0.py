class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # stores (start_index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, popped_height = stack.pop()
                width = i - index
                area = popped_height * width
                max_area = max(max_area, area)
                start = index
            stack.append((start, height))
        for index, height in stack:
            width = len(heights) - index
            area = height * width
            max_area = max(max_area, area)

        return max_area