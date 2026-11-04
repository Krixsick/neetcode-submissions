from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        fresh_fruit = 0
        timer = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1
        while queue and fresh_fruit > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                visited.add((row, col))
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc
                    if not (0 <= new_row < ROWS and 0 <= new_col < COLS): 
                        continue
                    if grid[new_row][new_col] != 1:
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 2
                    fresh_fruit -= 1
            timer += 1
        if fresh_fruit == 0:
            return timer
        else:
            return -1
                
        return timer
                