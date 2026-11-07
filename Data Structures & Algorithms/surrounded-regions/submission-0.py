from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(board), len(board[0])
        queue = deque([])
        visited = set()
        regions = set()

        top_and_left = ([(row, 0) for row in range(len(board))] + [(0, col) for col in range(len(board[0]))])
        bottom_and_right = ([(row, COLS - 1) for row in range(len(board))] + [(ROWS - 1, col) for col in range(len(board[0]))])

        for position in top_and_left:
            r, c = position
            if board[r][c] == "O":
                queue.append(position)
                visited.add(position)
                regions.add(position)
        for position in bottom_and_right:
            r, c = position
            if board[r][c] == "O":
                queue.append(position)
                visited.add(position)
                regions.add(position)
        while queue:
            r,c = queue.popleft()
            for dr, dc in DIRECTIONS:
                new_row, new_col = r + dr, dc + c
                if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    continue
                if (new_row, new_col) in visited:
                    continue
                if board[new_row][new_col] == "X":
                    continue
                regions.add((new_row, new_col))
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
        for row in range(len(board)):
            for col in range(len(board[row])):
                if (row, col) not in regions:
                    board[row][col] = "X"
        
