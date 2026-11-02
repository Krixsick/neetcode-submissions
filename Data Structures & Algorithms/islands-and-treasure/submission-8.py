class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque([])
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            counter = 0
            r,c = queue.popleft()
            visited.add((r, c))
            for dr, dc in DIRECTIONS:
                new_row, new_col = r + dr, c + dc
                if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    continue
                if grid[new_row][new_col] != INF:
                    continue
                

                queue.append((new_row, new_col))
                grid[new_row][new_col] = grid[r][c] + 1

