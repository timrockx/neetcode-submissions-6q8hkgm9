class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] in ["X", "#"]:
                return
            board[row][col] = "#"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        # dfs off any 0 on the border
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    if board[r][c] == "O":
                        dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"