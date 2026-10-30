from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [[1,0], [-1,0], [0, 1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        max_islands = 0

        def bfs(row, col):
            queue.append((row, col))
            visited.add((row, col))
            while queue:
                row, col = queue.popleft()
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc
                    if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                        continue
                    if grid[new_row][new_col] == "0":
                        continue
                    if (new_row, new_col) in visited:
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            return 
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    max_islands += 1
        return max_islands