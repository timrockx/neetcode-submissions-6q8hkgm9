class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        visited = set()

        # get indicies of all surrounded
        def dfs(row, col):

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] in ["X", "#"]:
                return            

            board[row][col] = "#"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)


        for row in range(rows):
            for col in range(cols):
                if row in [0, rows-1] or col in [0, cols-1] and board[row][col] == "O":
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"

        
        
