class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            middle = (l + r) // 2
            row, col = middle // COLS, middle % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False