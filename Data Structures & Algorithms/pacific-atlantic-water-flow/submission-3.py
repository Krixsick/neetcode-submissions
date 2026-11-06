from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [[1,0], [-1,0],[0,-1], [0,1]]
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(starting_cell):
            visited = set(starting_cell)
            queue = deque(visited)
            while queue:
                r, c = queue.popleft()
                for dr, dc in DIRECTIONS:
                    new_row, new_col = r + dr, dc + c
                    if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                        continue
                    if heights[new_row][new_col] < heights[r][c]:
                        continue
                    if (new_row, new_col) in visited:
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
            return visited
        pacific_starts = (
        [(r, 0) for r in range(ROWS)]
        + [(0, c) for c in range(COLS)]
    )

        atlantic_starts = (
            [(r, COLS - 1) for r in range(ROWS)]
            + [(ROWS - 1, c) for c in range(COLS)]
        )

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]