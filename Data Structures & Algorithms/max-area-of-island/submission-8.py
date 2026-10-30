class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return 0
            if grid[row][col] == 0:
                return 0
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            current_area = 1
            
            for dr, dc in DIRECTIONS:
                nr, nc = dr + row, dc + col
                current_area += dfs(nr, nc)
            return current_area
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1 and (i, j) not in visited):
                    current_area = dfs(i, j)
                    max_area = max(current_area, max_area)
        return max_area
                